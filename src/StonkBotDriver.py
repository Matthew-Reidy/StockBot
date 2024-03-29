import discord
from discord.ext import commands
from requestModule import dataModule
import os
from dotenv import load_dotenv
import time

load_dotenv('./config/.env')

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#DEV USE ONLY
#=====================
# @client.command()
# async def latency(ctx):
#     await ctx.send(client.latency )

#=====================

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@client.command(aliases = ['cmdlist'])
async def legend(ctx):
    await ctx.channel.send('all commands prefixed by $ symbol\nReturn daily movers: DailyMovers, DailyMovers, DM')
   

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   
   data = dataModule().getDMs()

   await ctx.send(data)
   

#retrieves ticker info
@client.command(aliases=['getQuote', 'getquote'])
async def GetTickerQuote(ctx, arg: str):

        params ={"region":"US", "symbol": arg}
        data = dataModule().getQuote(params)

        await ctx.send(data)

@client.command(aliases = ["earnings"])
#gets general earnings from the previous 6 months
async def getGeneralEarningsReport(ctx, ticker= None):
    if ticker != None:
        
        params= {
            "endpoint": "stock/v2/get-earnings",
            "symbol": ticker,
            "region": "US",
            "lang": "en-US"
        }
        data = dataModule().getEarningsData(params)
        await ctx.send(data)
    else:
        
        params= {
            "endpoint": "market/v2/get-earnings",
            "region": "US",
            "startDate": time.time() - 15778476000,
            "endDate": time.time(),
            "size": 10
        }
        data = dataModule().getEarningsData(params)
        await ctx.send(data)
    
    
@client.command(aliases = ["snapshot"])
async def marketSnapshot(ctx):
    data = dataModule().marketSnapShot()
    await ctx.send(data)

@client.command(aliases = ['markethours'])
async def MarketHours(ctx):
     await ctx.send('[New York](https://www.nyse.com/markets/hours-calendars)\n[London/Europe](https://www.londonstockexchange.com/equities-trading/business-days)\n[Japan/Asia](https://www.jpx.co.jp/english/corporate/about-jpx/calendar/index.html)')
     

client.run(os.getenv('DISCORD_KEY'))

