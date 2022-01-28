import discord
from discord.ext import commands 
import json
import random
import os

import core.classinit
from load import load

jdata = load('text')
class send_out ( core.classinit.Cog_Extension ) :

	@commands.command()
	async def 星爆語錄(self,ctx):
	    r_s = random.choice(jdata['sen'])
	    await ctx.send(r_s)

	@commands.command()
	async def 星爆圖(self,ctx):
	    r_p = random.choice(jdata['pic'])
	    await ctx.send(r_p)

def setup(bot):
    bot.add_cog(send_out(bot))