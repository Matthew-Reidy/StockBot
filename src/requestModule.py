import requests as request
import json
import os
from dotenv import load_dotenv
import math
load_dotenv('./config/.env')

class dataModule:
    def __init__(self) -> None:
        self.headers = {'x-rapidapi-key': os.getenv('RAPID_API_KEY'),'x-rapidapi-host': os.getenv('RAPID_API_HOST')}
        self.url= "https://apidojo-yahoo-finance-v1.p.rapidapi.com/"

    def getDMs(self):
        endpoint = 'market/v2/get-movers'
        result = request.get(self.url + endpoint, headers=self.headers)

        body = json.loads(result.text)

        bodylist = body["finance"]["result"]
        
        dailymovers: str = ""
        for elements in range(len(bodylist)):
            dailymovers += f'{bodylist[elements]["title"]} \n'
            quotelist = bodylist[elements]["quotes"]
            for i in range(len(quotelist)):
                dailymovers += f'\t {quotelist[i]["symbol"]} \n'
        return dailymovers
       

    def getQuote(self, param):
        endpoint = 'stock/v2/get-summary'
        summary: str = ""
        result = request.get(self.url+endpoint,headers=self.headers, params=param)
        print(result.status_code)
        body = json.loads(result.text)
        
        summary +=f'{param["symbol"]}\n{body["summaryProfile"]["city"]}, {body["summaryProfile"]["country"]} \n\n Price - ${body["price"]["regularMarketOpen"]["fmt"]}\n'
        earningsarr = body["earnings"]["earningsChart"]["quarterly"]
        for quarterlyEarnings in range(len(earningsarr)):
            rawActual =  earningsarr[quarterlyEarnings]["actual"]["raw"] 
            rawEstimate =  earningsarr[quarterlyEarnings]["estimate"]["raw"]
            summary += f'{earningsarr[quarterlyEarnings]["date"]}\n Estimated - {earningsarr[quarterlyEarnings]["estimate"]["fmt"]}, Actual- {earningsarr[quarterlyEarnings]["actual"]["fmt"]} '
            if rawActual <= rawEstimate:
                summary += f'Missed by {rawActual - rawEstimate}\n'
            else:
                summary += f'Beat by {rawActual - rawEstimate}\n'
        
        profitsyrly = body["earnings"]["financialsChart"]["yearly"]
        profitsqrtrly = body["earnings"]["financialsChart"]["quarterly"]
        for yearlyProfits in range(len(profitsyrly)):
            summary += f'{profitsyrly[yearlyProfits]["date"]} \n Revenue {profitsyrly[yearlyProfits]["revenue"]["fmt"]} - earnings {profitsyrly[yearlyProfits]["earnings"]["fmt"]}\n'
           
            for quarterlyProfits in range(len(profitsqrtrly)):
                if profitsyrly[yearlyProfits]["date"] == int(profitsqrtrly[quarterlyProfits]["date"][2:5]):
                    summary += f'\n\t earning{profitsqrtrly[quarterlyProfits]["earnings"]["fmt"]}, actual-{profitsqrtrly[quarterlyProfits]["revenue"]["fmt"]}'
            summary+="No quarterly data available for this year"
            

        return summary
       
    def marketSnapShot(self):
        endpoint = 'market/v2/get-summary'
        summary: str = ""
        result = request.get(self.url+endpoint,headers=self.headers)
        body = json.loads(result.text)

        filtered = body["marketSummaryAndSparkResponse"]["result"][0]

            
        print(filtered)

    def getEarningsData(self, param: dict):
        
        endpoint = f'{param["enpoint"]}/get-earnings'
        result = request.get(self.url + endpoint, headers=self.headers, params=param)

        body = json.loads(result.text)
        return body
        #todo parse JSON 


  
# params ={"region":"US", "symbol": "AMRN"}
# data = dataModule().getQuote(params)

# # dataModule().getDMs()

# print(dataModule().getDifference(actual=-0.18, estimate=-0.06))