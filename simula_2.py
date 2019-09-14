import random
from share_prices import SharePrices
from common import get_avg_price
from common import get_commision
from common import sign


def simula2(ticker: str, location: str):
    """An experiment with a little bit less stupid investment strategy"""

    sp = SharePrices()
    sp.load(ticker, location)
    data_size = len(sp.data)

    max_trans_len = 15
    max_trans_amount = 1000
    max_trans_count = 10
    max_loose = 0.10
    track_prev_count = 3

    cnt_trans = 0
    total_balance = 0.0
    cnt_win = 0
    cnt_loose = 0

    for n in range(1, 1 + max_trans_count):
        start_date = random.randint(0, data_size-max_trans_len)
        price1 = sp.data[start_date]
        buy = get_avg_price(price1.price_high, price1.price_low)
        if buy > max_trans_amount:
            continue
        n_shares = int(max_trans_amount / buy)
        total_buy = n_shares * buy + get_commision(n_shares, buy)

        prev_avg_price = buy
        deltas_track = [0] * track_prev_count
        pos = start_date + 1
        n_days = 0
        while pos < data_size:
            price2 = sp.data[pos]
            avg_price = get_avg_price(price2.price_high, price2.price_low)
            current_delta = avg_price - prev_avg_price
            deltas_track[pos % track_prev_count] = current_delta
            n_days += 1
            n_minuses = abs(sum([min(0, sign(v)) for v in deltas_track]))

            price_change = (avg_price - buy) / buy
            sell_signal = (price_change < -max_loose) \
                            or (pos + 1 == data_size) \
                            or (n_days > track_prev_count and n_minuses >= 3)

            if sell_signal:
                total_sell = n_shares * avg_price - get_commision(n_shares, avg_price)
                balance = total_sell - total_buy
                cnt_trans += 1
                total_balance += balance
                if balance >= 0:
                    cnt_win += 1
                else:
                    cnt_loose += 1
                break

            pos += 1
            prev_avg_price = avg_price

    print("Ticker: %s, transactions=%d, total balance=%.2f, wins=%d, loose=%d" % (ticker, cnt_trans, total_balance,
                                                                                  cnt_win, cnt_loose))
    return cnt_trans, total_balance, cnt_win, cnt_loose

