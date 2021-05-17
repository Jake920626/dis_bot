import discord
from discord import file
from discord.ext import commands
import json
import random

with open ( 'setting.json' , 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():
    print(">> bot is ready <<")

@bot.command()
async def starburst(ctx):
    r_s = random.choice(jdata['sen'])
    await ctx.send(r_s)

@bot.command()
async def starburst_pic(ctx):
    r_p = random.choice(jdata['pic'])
    await ctx.send(r_p)

@bot.command()
async def help_me(ctx):
    await ctx.send(jdata['help'])

bot.run(jdata['token'])