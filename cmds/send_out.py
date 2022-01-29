import discord
from discord.ext import commands 
import json
import random
import os

import core.classinit
from core.load import load

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

	@commands.command()
	async def 星爆圖全(self,ctx):
		for picture in jdata['pic']:
			await ctx.send(picture)

	@commands.command()
	async def 星爆語錄全(self,ctx):
		for sentence in jdata['sen']:
			await ctx.send(sentence)

	@commands.command()
	async def 星爆圖星爆我(self,ctx):
	    r_p = random.choice(jdata['pic'])
	    await ctx.author.send(r_p)

def setup(bot):
    bot.add_cog(send_out(bot))