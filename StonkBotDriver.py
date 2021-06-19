import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')


@client.event
async def on_ready():
    print('Sample output- bot active')

#DEV USE ONLY
#=====================
@client.command
async def latency(ctx):
    await ctx.send('{round(client.latency * 1000)}ms')
#=====================

@client.command(aliases = ['cmdlist'])
async def legend(ctx):
    await ctx.send('all commands prefixed by $ symbol\nReturn daily movers: DailyMovers, DailyMovers, DM')

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   await ctx.send('Test output')

@client.command
async def GetTicker(ctx):
    await ctx.send('test output')
    
client.run('ODU0MDcyMzQ3MzU4NjU4NTcw.YMem2w.sL01rRwKibWfQ13u0tjepcoZt3s')

