import random
from share_prices import SharePrices
from common import get_avg_price
from common import get_commision


def simula_random(ticker: str, location: str):
    """One investment strategy that is completely random! :) """

    sp = SharePrices()
    sp.load(ticker, location)
    data_size = len(sp.data)

    max_trans_len = 15
    max_trans_amount = 1000
    max_trans_count = 10

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

        end_date = start_date + random.randint(1, max_trans_len)
        price2 = sp.data[end_date]
        sell = get_avg_price(price2.price_high, price2.price_low)
        total_sell = n_shares * sell - get_commision(n_shares, sell)

        balance = total_sell - total_buy
        if balance >= 0:
            cnt_win += 1
        else:
            cnt_loose += 1
        cnt_trans += 1
        total_balance += balance

    print("Ticker: %s, transactions=%d, total balance=%.2f, wins=%d, loose=%d" % (ticker, cnt_trans, total_balance,
                                                                                  cnt_win, cnt_loose))
    return cnt_trans, total_balance, cnt_win, cnt_loose


