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

Required_list = dict()
with open('AdminRequired.json','r') as Required:
    Required_list = json.load(Required)

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
    print(ctx.author.id)
    if str(ctx.author.id) in jdata['admin']:
        bot.load_extension(F'cmds.{extension}')
        await ctx.send(F'{extension} loaded')
    else:
        await ctx.send('你沒有權限！')

@bot.command()
async def reload(ctx,extension):
    if str(ctx.author.id) in jdata['admin']:
        bot.reload_extension(F'cmds.{extension}')
        await ctx.send(F'{extension} reloaded')
    else:
        await ctx.send('你沒有權限！')

@bot.command()
async def unload(ctx,extension):
    if str(ctx.author.id) in jdata['admin']:
        bot.unload_extension(F'cmds.{extension}')
        await ctx.send(F'{extension} unloaded')
    else:
        await ctx.send('你沒有權限！')

#申請op指令
@bot.command()
async def op_required (ctx):
    global Required_list
    print(str(f'{ctx.author}'))
    if str(ctx.author.id) in jdata['admin']:#管理員不要亂
            await ctx.send('管理員申請屁喔！')
    else:
        if str(f'{ctx.author}') in Required_list:
            await ctx.send('請等待管理員確認喔！')
        else:
            Required_list[str(f'{ctx.author}')] = ctx.author.id
            with open('AdminRequired.json','w') as Required:
                json.dump(Required_list,Required)
            with open('AdminRequired.json','r') as Required:
                Required_list = json.load(Required)
            await ctx.send('已收到申請，請等待確認！')

#查看有誰申請
@bot.command()
async def op_required_list(ctx):
    if str(ctx.author.id) in jdata['admin']:
        for key in Required_list:
            await ctx.send(key)
    else:
        await ctx.send('你沒有權限！')

#確認申請
@bot.command()
async def op_allow(ctx,Requirment):
    global Required_list,jdata
    if str(ctx.author.id) in jdata['admin']:
        if Requirment in Required_list:#確認此人有申請
            jdata['admin'].append(str(Required_list[f'{Requirment}']))#增加入管理者列
            del Required_list[f'{Requirment}']#刪除待加入
            admin_update = {'admin':jdata['admin']} 
            with open('AdminRequired.json','w') as Required:
                json.dump(Required_list,Required)
            with open('AdminRequired.json','r') as Required:
                Required_list = json.load(Required)
            with open ('text/administrator.json','w') as write_in:
                json.dump(admin_update,write_in)#寫入json中儲存
            jdata = load('text')
            await ctx.send('歡迎'+str(f'{Requirment}')+'成為管理員！')
        else:
            await ctx.send('此人沒有申請喔！')
    else:
        await ctx.send('你沒有權限！')


for filename in os.listdir('cmds'):
    if filename[-3::]  == '.py':
        bot.load_extension(F"cmds.{filename[:-3]}")



print ('loaded')

print(jdata['admin'])

#keep_alive.keep_alive()

if __name__ == "__main__":
    bot.run(f'{Token}')