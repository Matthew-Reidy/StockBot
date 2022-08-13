
import requests
import json
import os

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"

headers = {
    'x-rapidapi-key': os.environ['RAPID_API_KEY'],
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }


#gets quote of 
def get_quote(self):
    querystring = {"q" : symbol ,"region":"US"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    data= json.loads(response)
     
    for quote in data['result']:
        print(quote['symbol', 'regularMarketPrice'])
         
#retreives daily movers
def get_DM(self):
    DMquerystring = {"region": "US"}
    DMresponse = requests.request("GET", url, headers=headers, params= DMquerystring)
    data=json.loads(DMresponse)

 
