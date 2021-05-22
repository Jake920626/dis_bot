import discord
from discord import file
from discord.ext import commands
import json
import random
import os
from dotenv import load_dotenv

token = os.getenv("token")

with open ( '/Users/apple/Documents/GitHub/dis_bot/setting.json' , 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():
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

@bot.command()
async def reload(ctx):
    
    with open ( '/Users/apple/Documents/GitHub/dis_bot/setting.json' , 'r' , encoding = 'utf8') as jfile:
        jdata = json.load(jfile)
    await ctx.send("reloaded")
bot.run(token)