import requests as request
import json
import os

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2"

headers = {
    'x-rapidapi-key': "",
    'x-rapidapi-host': ""
    }

def getDMs():
    endpoint = '/get-movers'
    result = request.get(url + endpoint,headers=headers)

    body = json.loads(result.text)

    bodylist = body["finance"]["result"]
  
    dailymovers: list[str] = []
    for elements in range(len(bodylist)):
        dailymovers.append(bodylist[elements]["title"])
        quotelist = bodylist[elements]["quotes"]
        for i in range(len(quotelist)):
            dailymovers.append(quotelist[i]["symbol"])
    return dailymovers


def getQuote(ticker):
    endpoint = '/get-quotes'
    result = request.get(url+endpoint,headers=headers)
    body= json.loads()
    
        
   
 
