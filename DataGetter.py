import StockBot
import requests
import json

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

headers = {
    'x-rapidapi-key': "f7f1e450bcmshdc0e3e81df6d6f3p1d2703jsn265972d33553",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }


class dataget:
    def __init__(self, symbol):
        self.ticker= symbol
      
        def get_quote(self):
         querystring = {"q" : symbol ,"region":"US"}
         response = requests.request("GET", url, headers=headers, params=querystring)
         data= json.loads(response)
     
         for quote in data['result']:
            print(quote['symbol', 'regularMarketPrice'])
         

         def get_DM(self):
          DMquerystring = {"region": "US"}
          DMresponse = requests.request("GET", url, headers=headers, params= DMquerystring)
          data=json.loads(DMresponse)

dg= dataget()
dg.get_quote()
