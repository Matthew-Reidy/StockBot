import discord
from discord.ext import commands
import requestModule
import os
from dotenv import load_dotenv
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
   
   data = requestModule.dataModule.getDMs()

   await ctx.send( "test" )
   

#retrieves ticker info
@client.command(aliases=['getQuote', 'getquote'])
async def GetTickerQuote(ctx, arg: str):
    if type(arg) != str and type(arg) == int or float:
        await ctx.send("unrecognized argument. please enter a ticker symbol")
    else:
        data = requestModule.dataModule.getQuote(arg)
        await ctx.send(data)

@client.command
async def getEarningsReport(ctx, arg:str):
    if type(arg) != str and type(arg) == int or float:
        await ctx.send("unrecognized argument. please enter a ticker symbol")
    else:
        params= {

        }
        data = requestModule.dataModule.getEarningsData(params)
   

@client.command(aliases = ['markethours'])
async def MarketHours(ctx):
     await ctx.send('https://www.nyse.com/markets/hours-calendars')
     

client.run(os.getenv('DISCORD_KEY'))

