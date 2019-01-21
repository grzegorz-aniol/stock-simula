import csv
from day_result import DayResult


class SharePrices:
    """Collection of all prices of a stock"""

    data = []

    def load(self, ticker, input_dir="d:/databases/wig/TOTAL"):
        self.data = []
        input_file = input_dir + "/" + ticker + ".csv"
        with open(input_file,"r") as input_file:
            cr = csv.reader(input_file)
            for row in cr:
                (date_str, price_open, price_high, price_low, price_close, volume) = row
                self.data.append(DayResult(date_str, float(price_open), float(price_high),
                                           float(price_low), float(price_close),
                                           float(volume)))


