from os import listdir
from os.path import isfile, join

from datetime import datetime, timedelta

from share_prices import SharePrices


def get_all_files(local_dir: str):
    ret_list = []
    for f in listdir(local_dir):
        if isfile(join(local_dir, f)) and f[-4:] == '.csv':
            ret_list.append(f[0:-4])
    return ret_list


def list_aggregates(somelist):
    min_value = None
    max_value = None
    avg_value = None
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


def run(_dir: str, tickers: list):
    """Calculates average value of 1Y profitability, during the whole history range, for particular stocks"""
    fmt = '%Y%m%d'
    for ticker in tickers:
        sp = SharePrices()
        sp.load(ticker, _dir)
#        data_size = len(sp.data)
#        print("Loading {}, size={}".format(ticker, data_size))
        last_date = datetime.strptime(sp.data[-1].date, fmt)
        first_date = datetime.strptime(sp.data[0].date, fmt)
        delta = last_date - first_date
        if delta > timedelta(weeks=52):  # at least 1 year of results
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
            for key, value in prices.items():
                future_date = key + timedelta(weeks=52)
                future_value = prices.get(future_date)
                if future_value:
                    rate = future_value/value - 1.0
                    results[key] = rate
#                    print(" {}[{:%Y%m%d}, {:%Y%m%d}] -> {:.2f}, {:.2f}, {:.4f}".format(ticker, key, future_date,
#                                                                      value, future_value,
#                                                                      rate))

            (min, max, avg) = list_aggregates(results.values())
            print("ticker={}, min={:.4f}, max={:.4f}, avg={:.4f}".format(ticker, min, max, avg))


if __name__ == '__main__':
    DIR = 'd:/databases/tfi/TOTAL'
    TICKERS = get_all_files(DIR)
    run(DIR, TICKERS)
