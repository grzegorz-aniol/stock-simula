import csv
from day_result import DayResult


class SharePrices:
    """Collection of all prices of a stock"""

    data = []
    desc = ""

    def load(self, ticker: str, input_dir: str, ext: str = '.txt', desc = ""):
        self.data = []
        self.desc = desc
        input_file = input_dir + "/" + ticker + ext
        with open(input_file,"r") as input_file:
            cr = csv.reader(input_file)
            next(cr, None) # Skip header
            for row in cr:
                (_, date_str, price_open, price_high, price_low, price_close, volume) = row
                self.data.append(DayResult(date_str, float(price_open), float(price_high),
                                           float(price_low), float(price_close),
                                           float(volume)))

    @staticmethod
    def load_descriptions(desc_file: str) -> map:
        data = {}
        with open(desc_file,"r") as input_file:
            cr = csv.reader(input_file, delimiter=' ')
            for v in range(1,4):
                next(cr, None)  # Skip header
            for row in cr:
                filtered = list(filter(lambda x: x, row))
                if len(filtered) < 5:
                    continue
                (file_id, *description) = filtered[4:]
                name = file_id[:-4]
                data[name]=' '.join(description)

        return data
