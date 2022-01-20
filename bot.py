import discord
from discord import file
from discord.ext import commands
import json
import random
import os
import keep_alive

jdata = {}
token = os.environ['token']
for filenames in os.listdir('dis_bot/text'):
    with open ( 'setting.json' , 'r' , encoding = 'utf8') as jfile:
        jdata.update(json.load(jfile))

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():

    game = discord.Activity(type = discord.ActivityType.playing,name = '刀劍神域')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)
    
    print(">> bot is ready <<")

@bot.command()
async def 星爆(ctx):
    r_s = random.choice(jdata['sen'])
    await ctx.send(r_s)

@bot.command()
async def 星爆圖(ctx):
    r_p = random.choice(jdata['pic'])
    await ctx.send(r_p)

@bot.command()
async def help_me(ctx):
    await ctx.send(jdata['help'])

keep_alive.keep_alive()
bot.run(token)