import pandas as pd

from pathlib import Path

if __name__ == '__main__':

    chemin_base = Path(__file__).parent
    chemin_bitcoin = chemin_base.joinpath("data", "crypto", "bitcoin.csv")

    df = pd.read_csv(chemin_bitcoin)
