# instructions to reproduce
1. create a folder "data" inside the repo, and two more "prices" and "tickers" inside it:
    C:.
    └───data
        ├───prices
        └───tickers 
2. go to https://www.slickcharts.com/sp500, save full page HTML to "data/tickers/sp500.txt"
3. run python get_tickers.py
4. run python refresh_prices.py
5. open main.ipynb and 