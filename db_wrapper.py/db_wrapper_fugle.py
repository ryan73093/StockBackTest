from fugle_marketdata import RestClient
import pandas as pd
import mplfinance as mpf
from base_wrapper import GetData

client = RestClient(api_key = 'ZGE0M2MxYTQtMmY5NC00MjE4LTg0OGYtZWU5ZmY0ZGFhNzVkIGEwMjVmNzFiLTZjMjgtNDI2Zi1iZjA5LTg2NDZkNzU0ODliYg==')
stock = client.stock
# data=stock.historical.stats(symbol = "0050")
# print(data)

class GetStockData(GetData):
    def __init__(self) -> None:
        super().__init__()

    def transfer_request_data(self,request_data):
        '''
        將request的資料 轉換為dataframe的形式，並進行調整
        '''


        # 将提供的数据转换为 pandas DataFrame
        df = pd.DataFrame(request_data['data'])
        
        # 确保日期列是日期类型
        df['date'] = pd.to_datetime(df['date'])
        df=df.sort_values(by='date',ascending=True)
        df=df.reset_index(drop=True)
        print(df)
        return df



    def get_stock_history(self,stock_id,start_date,end_date):

        '''
        parameter:
            stock_id: 0050
            start_date: 2023-01-01
            end_date: 2023-12-31
        
        '''

        request_data=stock.historical.candles(**{"symbol": stock_id,
                                        "from": start_date,
                                        "to": end_date,
                                        "fields": "open,high,low,close,volume,change,turnover"})
        df=self.transfer_request_data(request_data=request_data)
        print(df)
        return df




def plot_candle_figure(input_df):

    df=input_df.copy()
    # 设置日期为 DataFrame 的索引
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # 使用 mplfinance 绘制蜡烛图
    mpf.plot(df, type='candle', style='charles', 
            title='Candlestick Chart for 0050', 
            ylabel='Price')


get=GetStockData()
get.get_stock_history('2330','2023-01-01','2023-12-31')

# plot_candle_figure(df)




