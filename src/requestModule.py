import requests as request
import json
import os
from dotenv import load_dotenv

load_dotenv('./config/.env')

class dataModule:
    def __init__(self) -> None:
        self.headers = {'x-rapidapi-key': os.getenv('RAPID_API_KEY'),'x-rapidapi-host': os.getenv('RAPID_API_HOST')}
        self.url= "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2"

    def getDMs(self):
        endpoint = '/get-movers'
        result = request.get(self.url + endpoint, headers=self.headers)

        body = json.loads(result.text)

        bodylist = body["finance"]["result"]
        
        dailymovers: list[str] = []
        for elements in range(len(bodylist)):
            dailymovers.append(bodylist[elements]["title"])
            quotelist = bodylist[elements]["quotes"]
            for i in range(len(quotelist)):
                dailymovers.append(quotelist[i]["symbol"])
        return dailymovers
        #todo build a returnable string

    def getQuote(self, ticker: str) -> str:
        endpoint = '/get-quotes'
        params: dict[str,str] = {
                "symbols": ticker, 
                "region": "US"
                }
        result = request.get(self.url+endpoint,headers=self.headers, params=params)
        body= json.loads(result.text)
        print(body)
        #todo parse JSON 
        
    def getEarningsData(self, arg: dict):
        pass
   
 
