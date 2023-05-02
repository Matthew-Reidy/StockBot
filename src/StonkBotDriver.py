import discord
from discord.ext import commands
import requestModule
import os
from dotenv import load_dotenv
import time
load_dotenv('./config/.env')

client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#DEV USE ONLY
#=====================
@client.command()
async def latency(ctx):
    await ctx.send(client.latency )

#=====================

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@client.command(aliases = ['cmdlist'])
async def legend(ctx):
    await ctx.channel.send('all commands prefixed by $ symbol\nReturn daily movers: DailyMovers, DailyMovers, DM')
   

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   
   data = requestModule.dataModule().getDMs()

   await ctx.send(data)
   

#retrieves ticker info
@client.command(aliases=['getQuote', 'getquote'])
async def GetTickerQuote(ctx, arg: str):
    if type(arg) != str and type(arg) == int or float:
        await ctx.send("unrecognized argument. please enter a ticker symbol")
    else:
        params ={"region":"US", "symbols": arg}
        data = requestModule.dataModule().getQuote(params)

        await ctx.send(data)

@client.command(aliases = ["earnings"])
#gets general earnings from the previous 6 months
async def getGeneralEarningsReport(ctx):
        params= {
            "region": "US",
            "startDate": time.time() - 15778476000,
            "endDate": time.time(),
            "size": 10
        }
        data = requestModule.dataModule().getEarningsData(params)
        ctx.send(data)

@client.command(aliases=["Ticker earnings"])
#earnings report by ticker
async def getGeneralEarningsReport(ctx, arg:str):
    if type(arg) != str and type(arg) == int or float:
        await ctx.send("unrecognized argument. please enter a ticker symbol")
    else:
        params= {
            "region": "US",
            "startDate": time.time() - 15778476000,
            "endDate": time.time(),
            "size": 10
        }
        data = requestModule.dataModule().getEarningsData(params)
        ctx.send(data)

@client.command(aliases = ['markethours'])
async def MarketHours(ctx):
     await ctx.send('https://www.nyse.com/markets/hours-calendars')
     

client.run(os.getenv('DISCORD_KEY'))

