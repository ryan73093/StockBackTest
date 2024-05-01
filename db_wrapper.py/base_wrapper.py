import requests
import json

class GetData:
    def __init__(self) -> None:
        pass
    
    def get_api(self,request_url):
       
        response=requests.get(request_url)
        # 判斷該API呼叫是否成功
        if response.status_code != 200:
          raise Exception(f'error {response.status_code},取得股票資訊失敗.')
        else:
        #   print(response.text)
          pass

        # 將回傳的JSON格式資料轉成Python的dictionary
        data = json.loads(response.text)   
        return data 