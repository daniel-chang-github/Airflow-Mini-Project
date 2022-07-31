from datetime import date, timedelta
import yfinance as yf

def main(ticker,**kwargs):
    '''
    Function downloads the stock from Yahoo Finance with the parameter "stock_name"
    which define the particular stock we want to download.
    for example: "AAPL" for Apple stock or "TSLA" for Tesla stock
    HeaderList = 'Datetime', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'
    '''

    start_date = date.today()



    end_date = start_date + timedelta(days=1)
    df = yf.download(ticker, start=start_date, end=end_date, interval='1m')
    df.to_csv(ticker + "_data.csv", header=True)


if __name__ == '__main__':
    "dags/download_price.py"