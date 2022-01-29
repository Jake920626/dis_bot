import discord
from discord.ext import commands 
import json

import core.classinit
from core.load import load

jdata = load('text')

#建立update類別

class update ( core.classinit.Cog_Extension ) :

    #星爆圖更新指令
    @commands.command()
    async def 星爆圖更新(self,ctx,arg):
        global jdata
        print (arg)#確認網址為何
        jdata['pic'].append(arg)
        pic_update = {'pic':jdata['pic']} 
        with open ('text/picture.json','w') as write_in:
            json.dump(pic_update,write_in)#寫入json中儲存
        jdata = load('text')
        await ctx.send('增加成功！')

    #星爆語錄更新指令
    @commands.command()
    async def 星爆語錄更新(self,ctx,arg):
        global jdata
        print (arg)
        jdata['sen'].append(arg)
        sen_update = {'sen':jdata['sen']} 
        with open ('text/quotes.json','w') as write_in:
            json.dump(sen_update,write_in)#寫入json中儲存
        jdata = load('text')
        await ctx.send('增加成功！')

def setup(bot):
    bot.add_cog(update(bot))
