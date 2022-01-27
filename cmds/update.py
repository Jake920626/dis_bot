import discord
from discord.ext import commands 
import json

import core.classinit
from load import load

jdata = load()
class update ( core.classinit.Cog_Extension ) :
    @commands.command()
    async def 星爆圖更新(self,ctx,arg):
        global jdata
        print (arg)
        jdata['pic'].append(arg)
        pic_update = {'pic':jdata['pic']} 
        with open ('text/picture.json','w') as write_in:
            json.dump(pic_update,write_in)
        jdata = load()
        await ctx.send('增加成功！')

def setup(bot):
    bot.add_cog(update(bot))
