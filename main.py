from turtle import update
import discord
from discord.ext import commands
import json
import random
import os
#import keep_alive
from load import load

Token  = str()
t = {}
with open ('token.json',"r") as tk:
    t = json.load(tk)
    print (t)
    Token = str(t['token'])

jdata = {}
#token = os.environ['token']

jdata = load('text')

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():

    game = discord.Activity(type = discord.ActivityType.playing,name = '刀劍神域')

    await bot.change_presence(status=discord.Status.idle, activity=game)
    
    print(">> bot is ready <<")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(F'cmds.{extension}')
    await ctx.send(F'{extension} loaded')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(F'cmds.{extension}')
    await ctx.send(F'{extension} reloaded')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(F'cmds.{extension}')
    await ctx.send(F'{extension} unloaded')

for filename in os.listdir('cmds'):
    if filename[-3::]  == '.py':
        bot.load_extension(F"cmds.{filename[:-3]}")

print ('loaded')


#keep_alive.keep_alive()

if __name__ == "__main__":
    bot.run(f'{Token}')