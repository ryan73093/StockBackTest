import requests
import json
import pandas as pd
from base_wrapper import GetData

# request_url="https://openapi.twse.com.tw/v1/opendata/t187ap46_L_7" 

class GetStockData(GetData):
    def __init__(self) -> None:
        self.df_api=self.get_overall_data()

    def get_overall_data(self):

        '''
        取得API的詳細資訊
        '''
        request_url="https://openapi.twse.com.tw/v1/swagger.json"
        response=requests.get(request_url)
        # 判斷該API呼叫是否成功
        if response.status_code != 200:
          raise Exception('取得股票資訊失敗.')
        else:
        #   print(response.text)
          pass

        # 將回傳的JSON格式資料轉成Python的dictionary
        data = json.loads(response.text)
        # print(data)
        data_paths=data['paths']
        df_all_data=pd.DataFrame()
        for api in data_paths.keys():
            dict_api=data_paths[api]['get']
            tags=dict_api['tags']
            summary=dict_api['summary']
            description=dict_api['description']
            df_new_row=pd.DataFrame({
              'API':api,
              'Tag':tags,
              'Summary':summary,
              'Description':description
            })
            df_all_data=pd.concat([df_all_data,df_new_row],axis=0)
        print(df_all_data)
        return df_all_data
    
    def get_list_all_data(self):
        df=self.df_api
        lst_all_data=list(df['Summary'])
        print(lst_all_data)

    def get_data_by_summary(self,summary):

        df_over_all=self.df_api
        api=df_over_all[df_over_all['Summary']==summary].reset_index()['API'][0]
        request_url=f'https://openapi.twse.com.tw/v1{api}'
        print(request_url)
        data=self.get_api(request_url=request_url)
        print(data)
        return data

    def get_twse_news(self):
        dict_data=self.get_data_by_summary('證交所新聞')
        df = pd.DataFrame(dict_data)
        df=df[['Date','Title','Url']]
        print(df)
        return df
    
    def get_stock_news(self):
        dict_data=self.get_data_by_summary('上市公司每日重大訊息')
        df = pd.DataFrame(dict_data)
        print(df)
        return df

    def get_closing_price_and_monthly_price(self):
        dict_data=self.get_data_by_summary('上市個股日收盤價及月平均價')
        df = pd.DataFrame(dict_data)
        print(df)
        return df
       
    def get_closing_price_summary(self):
        dict_data=self.get_data_by_summary('每日收盤行情-大盤統計資訊')
        df = pd.DataFrame(dict_data)
        print(df)
        return df
    
    def get_company_info(self):
        dict_data=self.get_data_by_summary('上市公司基本資料')
        df = pd.DataFrame(dict_data)
        print(df)
        return df
    
    def get_daily_price(self):
        dict_data=self.get_data_by_summary('上市個股日成交資訊')
        df = pd.DataFrame(dict_data)
        print(df)
        return df

    def get_electric_trade_stastic(self):
        dict_data=self.get_data_by_summary('電子式交易統計資訊')
        df = pd.DataFrame(dict_data)
        print(df)
        return df



get=GetStockData()

# get.get_daily_price()
get.get_electric_trade_stastic()
# get.get_company_info()
# get.get_closing_price_summary()
# get.get_stock_news()
# get.get_data_by_summary('臺灣 50 指數歷史資料')
# get.get_data_by_summary('上市個股日收盤價及月平均價')
# get.get_stock_news()
# get.get_closing_price_and_monthly_price()


get.get_list_all_data()

