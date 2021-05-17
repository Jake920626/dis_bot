import discord
from discord import file
from discord.ext import commands
import json

with open ( 'setting.json' , 'r' , encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='! ')

@bot.event
async def on_ready():
    print(">> bot is ready <<")

@bot.command()
async def starburst(ctx):
    await ctx.send('faster')

@bot.command()
async def starburst_pic(ctx):
    await ctx.send(jdata['pic'])

bot.run(jdata['token'])