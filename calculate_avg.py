from os import listdir
from os.path import isfile, join

from datetime import datetime, timedelta

from share_prices import SharePrices

import numpy as np


def get_all_files(local_dir: str, ext = '.txt'):
    ret_list = []
    for f in listdir(local_dir):
        file_path = local_dir + "/" + f
        if isfile(file_path) and f[-4:] == '.txt':
            ret_list.append(f[0:-4])
    return ret_list


def list_aggregates(somelist) -> (float, float, float):
    min_value = None
    max_value = None
    if len(somelist) == 0:
        return None, None, None
    sum = 0
    for value in somelist:
        sum += value
        if not min_value or value < min_value:
            min_value = value
        if not max_value or value > max_value:
            max_value = value
    avg_value = sum / len(somelist)
    return min_value, max_value, avg_value


def analyze_avg_roi(sp: SharePrices, roi_period: timedelta = timedelta(weeks = 52),
                    past_history: timedelta = timedelta(weeks = 100*52)):
    """Calculates average ROI (as 1Y ROI) of profitability measured for provided ranges,
        during specific history range, for particular stock"""
    if past_history < roi_period:
        return None
    fmt = '%Y%m%d'
    last_date = datetime.strptime(sp.data[-1].date, fmt)
    first_date = datetime.strptime(sp.data[0].date, fmt)
    delta = last_date - first_date
    roi_to_year_adjustment = float(365 / roi_period.days)
    if delta < roi_period:  # minimal set of data
        return None

    prices = {}

    for index, day_result in enumerate(sp.data):
        value = day_result.price_close
        try:
            next_date = sp.data[index+1].dt
        except IndexError:
            next_date = day_result.dt + timedelta(days=1)
        d = day_result.dt
        while d < next_date:
            prices[d] = value
            d += timedelta(days=1)

    results = {}

    new_first_date = last_date - past_history
    if new_first_date > first_date:
        first_date = new_first_date

    key = first_date
    while key <= last_date:
        value = prices[key]
        future_date = key + roi_period
        future_value = prices.get(future_date)
        if future_value:
            rate = future_value/value - 1.0
            results[key] = roi_to_year_adjustment * rate
#                    print(" {}[{:%Y%m%d}, {:%Y%m%d}] -> {:.2f}, {:.2f}, {:.4f}".format(ticker, key, future_date,
#                                                                      value, future_value,
#                                                                      rate))
        else:
            break

        key += timedelta(days=1)

    values = [ v for v in results.values() ]
    (p0, p10, p50, p90, p100) = [ 100 * v for v in np.percentile(values, q=(0, 10, 50, 90, 100)) ]
    if p0 is None:
        return

    print("ticker={}, min={:.1f}%, p10={:.1f}%, p50={:.1f}%, p90={:.1f}%, max={:.1f}%, {}".format(ticker, p0, p10, p50, p90, p100, sp.desc))


def years(y: int) -> timedelta:
    return timedelta(weeks = 52 * y)


def months(m: int) -> timedelta:
    return timedelta(weeks = 4 * m)


if __name__ == '__main__':
    DIR = '/mnt/d/databases/tfi/omegafun'
    TICKERS = get_all_files(DIR)
    # TICKERS = ["AIG001"]

    DESC = SharePrices.load_descriptions(DIR + '/../omegafun.lst')

    for ticker in TICKERS:
        sp = SharePrices()
        sp.load(ticker, DIR, desc = DESC[ticker])
        analyze_avg_roi(sp, roi_period = months(3), past_history = years(5))
