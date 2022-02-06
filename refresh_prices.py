import yfinance as yf
import time

import pandas as pd
import numpy as np

def get_prices(fname, period="2y", col_name="ticker"):

    df = pd.read_csv(f'data/tickers/{fname}.csv')

    assets = df.loc[:, col_name].values
    prices = yf.download(" ".join(assets), period=period)["Adj Close"]

    prices.to_csv(f"data/prices/{fname}.csv")

def main():
    get_prices("sp500")

if __name__ == "__main__":
    main()
