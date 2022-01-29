import discord
from discord.ext import commands 
import json
import random
import os

import core.classinit
from core.load import load

jdata = {}

jdata = load('text')

Required_list = jdata['admin_required']

class op_control (core.classinit.Cog_Extension):

	#申請op指令
	@commands.command()
	async def op_require (self,ctx):
	    global Required_list,jdata
	    print(str(f'{ctx.author}'))
	    if str(ctx.author.id) in jdata['admin']:#管理員不要亂
	            await ctx.send('管理員申請屁喔！')
	    else:
	        if str(f'{ctx.author}') in Required_list:
	            await ctx.send('請等待管理員確認喔！')
	        else:
	            Required_list[str(f'{ctx.author}')] = ctx.author.id
	            with open('text/AdminRequired.json','w') as Required:
	                json.dump(Required_list,Required)
	            with open('text/AdminRequired.json','r') as Required:
	                Required_list = json.load(Required)
	            jdata = load('text')
	            await ctx.send('已收到申請，請等待確認！')

	#查看有誰申請
	@commands.command()
	async def op_required_list(self,ctx):
	    if str(ctx.author.id) in jdata['admin']:
	        for key in Required_list:
	            await ctx.send(key)
	    else:
	        await ctx.send('你沒有權限！')

	#確認申請
	@commands.command()
	async def op_allow(self,ctx,Requirment):
	    global Required_list,jdata
	    if str(ctx.author.id) in jdata['admin']:
	        if Requirment in Required_list:#確認此人有申請
	            jdata['admin'].append(str(Required_list[f'{Requirment}']))#增加入管理者列
	            del Required_list[f'{Requirment}']#刪除待加入
	            admin_update = {'admin':jdata['admin']} 
	            Required_update = {'admin_required':jdata['admin_required']}
	            with open('texy/AdminRequired.json','w') as Required:
	                json.dump(Required_update,Required)
	            with open ('text/administrator.json','w') as write_in:
	                json.dump(admin_update,write_in)#寫入json中儲存
	            jdata = load('text')
	            Required_list = jdata['admin_required']
	            await ctx.send('歡迎'+str(f'{Requirment}')+'成為管理員！')
	        else:
	            await ctx.send('此人沒有申請喔！')
	    else:
	        await ctx.send('你沒有權限！')


	#拔除資格
	@commands.command()
	async def op_deprive (self,ctx,Requirment):
		global jdata
		if str(ctx.author.id) in jdata['admin']:
			exist = False
			for id in jdata['admin']:
				user = await self.bot.fetch_user(id)#抓管理員的名字
				print(user)
				print (Requirment)
				if str(user) == str(Requirment):
					exist = True
					jdata['admin'].remove(id)
					admin_update = {'admin':jdata['admin']} 
					with open ('text/administrator.json','w') as write_in:
						json.dump(admin_update,write_in)#寫入json中儲存
					jdata = load('text')
					await ctx.send('已將'+str(f'{Requirment}')+'從管理員中剔除！')
			if exist == False:
				await ctx.send('此人不是管理員。')
		else:
			await ctx.send('你沒有權限！')



def setup(bot):
    bot.add_cog(op_control(bot))