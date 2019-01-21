from simula_random import simula_random
from simula_2 import simula2

def run():
    """Main function to run simulation"""

    tickers = ['LPP', 'INVESTORMS', 'PEKAO', 'KGHM', 'INGBSK','KETY','WAWEL','BZWBK','PZU','STALPROD','PKOBP','CCC', 'BOGDANKA','PKNORLEN','BUDIMEX','PGE', 'PULAWY',
    'AMICA','HANDLOWY','CYFRPLSAT','LOTOS','INTERCARS','EUROCASH','AMREST','ASSECOPOL','COMARCH','CEZ', 'ENEA','KERNEL','CIECH','ZPUE','NEUCA','ELBUDOWA',
    'APATOR','GROCLIN','ASTARTA','PEP', 'ORBIS']

    total_trans = 0
    total_balance = 0.0;
    cnt_win = 0
    cnt_loose = 0

    for ticker in tickers:
        (ct, tb, cw, cl) = simula_random(ticker)
        total_trans += ct
        total_balance += tb
        cnt_win += cw
        cnt_loose += cl

    print("TOTAL: transactions=%d, total balance=%.2f, wins=%d, loose=%d" % (total_trans, total_balance, cnt_win, cnt_loose))


if __name__ == '__main__':
    run()
