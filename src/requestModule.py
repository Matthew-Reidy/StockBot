import requests as request
import json
import os
from dotenv import load_dotenv
import math
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
        
        dailymovers: str = ""
        for elements in range(len(bodylist)):
            #dailymovers.append(bodylist[elements]["title"])
            dailymovers += bodylist[elements]["title"] + "\n"
            quotelist = bodylist[elements]["quotes"]
            for i in range(len(quotelist)):
                #dailymovers.append(quotelist[i]["symbol"])
                dailymovers += "\t" + quotelist[i]["symbol"] + "\n" 
        return dailymovers

    def getQuote(self, param: str) -> str:
        endpoint = '/get-quotes'

        result = request.get(self.url+endpoint,headers=self.headers, params=param)
        body= json.loads(result.text)
        return body
        #todo parse JSON 
        
    def getEarningsData(self, args: dict):
        endpoint = '/get-earnings'
        result = request.get(self.url + endpoint, headers=self.headers, params=args)

        body = json.loads(result.text)
        return body
        #todo parse JSON 

    def getEarningsByTicker(self, args: dict):
        endpoint = '/get-earnings'
        result = request.get(self.url + endpoint, headers=self.headers, params=args)

        body = json.loads(result.text)
        return body
        #todo parse JSON 
    
    def getDifference(self, actual: float, estimate: float) -> float:
        absOfNumerator: float = math.fabs(actual - estimate)
        divDenomenator: float = (actual + estimate) / 2

        diff: float =  (absOfNumerator / divDenomenator) * 100
        return diff
  
