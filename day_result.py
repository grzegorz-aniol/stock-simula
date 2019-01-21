from datetime import datetime


class DayResult:
    def __init__(self, date, po, ph, pl, pc, v):
        fmt = '%Y%m%d'
        self.dt = datetime.strptime(date, fmt)
        self.date = date
        self.price_open = po
        self.price_high = ph
        self.price_low = pl
        self.price_close = pc
        self.volume = v

