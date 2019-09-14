import csv
import glob
from collections import defaultdict
# from datetime import datetime
from typing import Any

from day_result import DayResult


def transform_results(input_dir: str, output_dir: str, all_years: list, extension: str = 'prn'):
    """Transforms data from date-oriented files into company-oriented files."""
    stocks = defaultdict(dict)  # type: defaultdict[Any, dict]

    for year in all_years:
        print("Year: %s" % year)
        allfiles = glob.glob("%s/%d/*.%s" % (input_dir, year, extension))
        for file_name in allfiles:
            cr = csv.reader(open(file_name, "r"))
            for row in cr:
                (ticker, date_str, price_open, price_high, price_low, price_close, volume) = row
    #            objDate = datetime.strptime(date_str, '%y%m%d')
                stocks[ticker][date_str] = DayResult(price_open, price_high, price_low, price_close, volume)

    for ticker in stocks.keys():
        prices = stocks[ticker]
        output_file = open(output_dir + "/" + ticker + ".csv", "w")
        cw = csv.writer(output_file, lineterminator='\n')
        for k, dr in prices.items():
            cw.writerow([k, dr.price_open, dr.price_high, dr.price_low, dr.price_close, dr.volume])
    #        cw.writerow([datetime.strftime(k, "%y-%m-%d"), v])
        output_file.close()


# transform_results(input_dir = "d:/databases/wig", output_dir = "d:/databases/wig/TOTAL",
#                   all_years = range(2010, 2019))

# transform_results(input_dir = "d:/databases/tfi", output_dir = "d:/databases/tfi/TOTAL",
#                  all_years = range(2007, 2019), extension = 'txt')

