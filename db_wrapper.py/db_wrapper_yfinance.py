import pandas as pd
import yfinance as yf
from base_wrapper import GetData


class GetStockData(GetData):
    def __init__(self) -> None:
        super().__init__()
    
    def get_stock_history(self,stock_id):
        data=yf.Ticker(stock_id)
        df=data.history(period='max').reset_index()
        print(df)
        return df

get=GetStockData()
get.get_stock_history('2330')