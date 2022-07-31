import pandas as pd
from datetime import datetime,timedelta

date = str(datetime.today().date())
LOCAL_DIR = 'tmp/data/' + date

def main():
    """ Function that calculates the difference between the day's open and closing price.
    Formula: day's diff = Adjusted close - open price
    """

    apple_data = pd.read_csv(LOCAL_DIR + "/AAPL_data.csv")  #.sort_values(by = "Datetime", ascending = False)
    tesla_data = pd.read_csv(LOCAL_DIR + "/TSLA_data.csv")  #.sort_values(by = "Datetime", ascending = False)

    spread = [  {'Apple': (apple_data['Adj Close'].iloc[-1] - apple_data['Open'].iloc[0])}   ,               
                {'Tesla': tesla_data['Adj Close'].iloc[-1] - tesla_data['Open'].iloc[0]  } ]

    with open(f"{LOCAL_DIR}/spread.txt", "w") as txtfile:
        txtfile.write(str(spread))
        txtfile.close()


if __name__ == '__main__':
    "dags/get_latest_spread.py"

