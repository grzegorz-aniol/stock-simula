from simula_random import simula_random
from simula_2 import simula2


def run():
    """Main function to run simulation"""

    stock_tickers = ['LPP', 'INVESTORMS', 'PEKAO', 'KGHM', 'INGBSK','KETY','WAWEL','BZWBK','PZU','STALPROD','PKOBP','CCC', 'BOGDANKA','PKNORLEN','BUDIMEX','PGE', 'PULAWY',
    'AMICA','HANDLOWY','CYFRPLSAT','LOTOS','INTERCARS','EUROCASH','AMREST','ASSECOPOL','COMARCH','CEZ', 'ENEA','KERNEL','CIECH','ZPUE','NEUCA','ELBUDOWA',
    'APATOR','GROCLIN','ASTARTA','PEP', 'ORBIS']

    # UI_021.txt        Generali Akcje Malych i Srednich Spolek
    tfi_tickers = ['UI_021']
    tfi_location = "/mnt/d/databases/tfi/omegafun"

    total_trans = 0
    total_balance = 0.0;
    cnt_win = 0
    cnt_loose = 0

    for ticker in tfi_tickers:
        (ct, tb, cw, cl) = simula_random(ticker, tfi_location)
        total_trans += ct
        total_balance += tb
        cnt_win += cw
        cnt_loose += cl

    print("TOTAL: transactions=%d, total balance=%.2f, wins=%d, loose=%d" % (total_trans, total_balance, cnt_win, cnt_loose))


if __name__ == '__main__':
    run()
