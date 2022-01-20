import discord
from discord import file
from discord.ext import commands
import json
import random
import os
import keep_alive
from load import load

jdata = {}
token = os.environ['token']

jdata = load()

bot = commands.Bot(command_prefix='!10 ')

@bot.event
async def on_ready():

    game = discord.Activity(type = discord.ActivityType.playing,name = '刀劍神域')

    await bot.change_presence(status=discord.Status.idle, activity=game)
    
    print(">> bot is ready <<")

@bot.command()
async def 星爆語錄(ctx):
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
async def 星爆圖更新(ctx,arg):
    global jdata
    print (arg)
    jdata['pic'].append(arg)
    pic_update = {'pic':jdata['pic']} 
    with open ('text/picture.json','w') as write_in:
        json.dump(pic_update,write_in)
    jdata = load()
    await ctx.send('增加成功！')

@bot.command()
async def 重整(ctx):
    global jdata
    jdata = load()
    await ctx.send('重整結束')

@bot.command()
async def 星爆語錄更新(ctx,arg):
    global jdata
    print (arg)
    jdata['sen'].append(arg)
    sen_update = {'sen':jdata['sen']} 
    with open ('text/quotes.json','w') as write_in:
        json.dump(sen_update,write_in)
    jdata = load()
    await ctx.send('增加成功！')

keep_alive.keep_alive()
bot.run(token)