import discord
from discord.ext import commands 
import json
import random
import os

import core.classinit
from core.load import load

jdata = load('text')

#建立control類別
class control ( core.classinit.Cog_Extension ) :

	@commands.command()
	async def help_me(self,ctx):
	    await ctx.send(jdata['help'])

	@commands.command()
	async def 重整(ctx):
	    global jdata
	    jdata = load('text')
	    await ctx.send('重整結束')

	@commands.command()
	async def test(self,ctx):
		print(ctx.author)
		await ctx.send(str(ctx.author.mention))

def setup(bot):
    bot.add_cog(control(bot))