# instructions to reproduce
1. create a folder "data" inside the repo, and two more "prices" and "tickers" inside it:
```bash
C:.
└───data
    ├───prices
    └───tickers 
```
2. go to https://www.slickcharts.com/sp500, save full page HTML to "data/tickers/sp500.txt":
```bash
C:.
└───data
    ├───prices
    └───tickers
        └───sp500.txt 
```
3. install requirements
```bash
pip install -r requirements.txt
```
4. run the following commands
```bash
python get_tickers.py
python refresh_prices.py
```
5. open main.ipynb and run it
