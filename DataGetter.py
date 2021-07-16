import StockBot
import requests

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

headers = {
    'x-rapidapi-key': "f7f1e450bcmshdc0e3e81df6d6f3p1d2703jsn265972d33553",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }



def getQuote(tick):
    querystring = {"q" : tick ,"region":"US"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

def getDM():
    DMquerystring = {"region": "US"}
    DMresponse = requests.request("GET", url, headers=headers, params= DMquerystring)
    print(DMresponse.text)
