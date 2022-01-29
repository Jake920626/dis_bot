from turtle import update
import discord
from discord.ext import commands
import json
import random
import os
#import keep_alive
from core.load import load

jdata = {}
#token = os.environ['token']

jdata = load('text')

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():

    game = discord.Activity(type = discord.ActivityType.playing,name = '刀劍神域')

    await bot.change_presence(status=discord.Status.online, activity=game)
    
    print(">> bot is ready <<")


for filename in os.listdir('cmds'):
    if filename[-3::]  == '.py':
        bot.load_extension(F"cmds.{filename[:-3]}")

#keep_alive.keep_alive()

Token = jdata['token']

if __name__ == "__main__":
    bot.run(f'{Token}')