
def get_avg_price(ph, pl):
    """Daily average prices calculated as an average of highest and lowest prices"""
    return (ph + pl)/2


def get_commision(n, price):
    """"""
    return max(3.0, 0.0039 * n * price)


def sign(val):
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0

