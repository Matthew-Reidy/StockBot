import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')


@client.event
async def on_ready():
    print('Sample output- bot active')


@client.command 
async def legend(ctx):
    await ctx.send('Return daily movers: $DailyMovers, DailyMovers, DM')

@client.command(aliases = ['DailyMover', 'DailyMovers'])
async def DM(ctx):
   await ctx.send('Test')

    
client.run('ODU0MDcyMzQ3MzU4NjU4NTcw.YMem2w.sL01rRwKibWfQ13u0tjepcoZt3s')

