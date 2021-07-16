import discord
from discord.ext import commands
import DataGetter

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('bot active')

#DEV USE ONLY
#=====================
@client.command()
async def latency(ctx):
    await ctx.send('{round(client.latency * 1000)}')
#=====================

@client.command(aliases = ['cmdlist'])
async def legend(ctx):
    await ctx.send('all commands prefixed by $ symbol\nReturn daily movers: DailyMovers, DailyMovers, DM')

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   await ctx.send(DataGetter.getDM)

#retrieves ticker info
@client.command()
async def GetTicker(ctx, msg):
    tick=msg
    DataGetter.GetQuote(tick)

@client.command(aliases = ['markethours'])
async def MarketHours(ctx):
     await ctx.send('https://www.nyse.com/markets/hours-calendars')


#dummy discord token    
client.run('ODU0MDcyMzQ3MzU4NjU4NTcw.YMem2w.sL01rRwKibWfQ13u0tjepcoZt3s')

