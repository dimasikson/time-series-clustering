import pandas as pd
import bs4
import io

def sp500_tickers():

    with io.open('data/tickers/sp500.txt', mode="r", encoding="utf-8") as f:
        webpage = f.read()
        soup, rows = bs4.BeautifulSoup(webpage, features="lxml"), []
        f.close()

    df = pd.DataFrame(columns=["num","name","ticker","weight","price","chg","pct_chg"])

    for i, tr in enumerate(soup.findAll("tr")):
        tds = [t.getText().strip() for t in tr.findAll("td")]
        if tds: df.loc[i, :] = tds

    return df.drop(columns=["num"])

def main():
    sp500_tickers().to_csv('data/tickers/sp500.csv', index=False)

if __name__ == "__main__":
    main()
