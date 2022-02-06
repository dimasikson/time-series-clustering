# time series clustering
<img width="820" alt="image" src="https://user-images.githubusercontent.com/47122797/152696979-f7a9a54b-a1ec-4a4b-8f50-dfce3db66c07.png">
chart 1. clusters of possible stock movement patterns.

## Q: what is this repo?
### A: this is an attempt to cluster patterns in stock prices, partly inspired by daytrading patterns such as below:

![image](https://user-images.githubusercontent.com/47122797/152697098-e7698fb0-3f14-48d1-9620-dbf623fe7247.png)

## Q: how?
#### step 1: sample random 30-day periods of a random stock from the S&P500
#### step 2: standardize the samples price
#### step 3: cluster the resulting dataset using KMeans
#### step 4(TBD): for a given stock, identify which pattern the stock price is currently in. then use that to forecast the next N days' price.

## Q: why?
### A: for fun mostly. later on I'd like to test predictive power of this approach compares to cutting edge time series methods.

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
