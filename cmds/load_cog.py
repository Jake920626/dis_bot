import discord
from discord.ext import commands 
import json
import random
import os

import core.classinit
from core.load import load

jdata = {}

jdata = load('text')

class load_cog(core.classinit.Cog_Extension):

	@commands.command()
	async def load(self,ctx,extension):
	    print(ctx.author.id)
	    if str(ctx.author.id) in jdata['admin']:
		    try:
		        self.bot.load_extension(F'cmds.{extension}')
		        await ctx.send(F'{extension} loaded')
		    except:await ctx.send('沒有此類別！')
	    else:
	        await ctx.send('你沒有權限！')

	@commands.command()
	async def reload(self,ctx,extension):
	    if str(ctx.author.id) in jdata['admin']:
		    try:
		        self.bot.reload_extension(F'cmds.{extension}')
		        await ctx.send(F'{extension} reloaded')
		    except:
	    		await ctx.send('沒有此類別！')
	    else:
	        await ctx.send('你沒有權限！')

	@commands.command()
	async def unload(self,ctx,extension):
	    if str(ctx.author.id) in jdata['admin']:
	    	if extension == 'load_cog' or extension == 'op_control':
	    		await ctx.send('此類別無法unload！')
	    	else:
	    		try:
	    			self.bot.unload_extension(F'cmds.{extension}')
	    			await ctx.send(F'{extension} unloaded')
	    		except:
	    			await ctx.send('沒有此類別！')
	        	
	    else:
	        await ctx.send('你沒有權限！')


def setup(bot):
    bot.add_cog(load_cog(bot))