import discord
from discord.ext import commands
import requestModule
client = commands.Bot(command_prefix='$')


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
#     await ctx.send(client.latency)
#     client.run()
#=====================

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)
    
@client.command(aliases = ['cmdlist'])
async def legend(ctx):
    await ctx.channel.send('all commands prefixed by $ symbol\nReturn daily movers: DailyMovers, DailyMovers, DM')
   

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   dms = ""
   payload = requestModule.getDMs()

   await ctx.send( "test" )
   

#retrieves ticker info
@client.command(aliases=['getQuote', 'getquote'])
async def GetTickerQuote(ctx, msg):
   
    pass
   

@client.command(aliases = ['markethours'])
async def MarketHours(ctx):
     await ctx.send('https://www.nyse.com/markets/hours-calendars')
     

client.run()

