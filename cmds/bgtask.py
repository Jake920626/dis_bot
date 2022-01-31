import discord
from discord.ext import commands , tasks
import json
import random
import os,datetime

import core.classinit
from core.load import load

jdata = {}

jdata = load('text')

class bgtask (core.classinit.Cog_Extension):

    def __init__(self,bot):
        super().__init__(bot)
        self.channels = []
        self.now = datetime.datetime.now().strftime('%H:%M:%S')
        self.used = False

    @commands.command()
    async def set_channel(self,ctx):
        if str(ctx.author.id) in jdata['admin']:
            if ctx.channel.id not in self.channels: 
                self.channels.append(ctx.channel.id) 
                await ctx.send('設定完畢')
            else:
                await ctx.send('已設定過')
        else:
            await ctx.send('你沒有權限！')

    @commands.command()
    async def start_loop(self,ctx):
        if str(ctx.author.id) in jdata['admin']:
            if self.ever_day_48763.is_running():
                await ctx.send('已在執行')
            else:
                self.ever_day_48763.start()
                await ctx.send('迴圈開始')
        else:
            await ctx.send('你沒有權限！')

    @commands.command()
    async def stop_loop(self,ctx):
        if str(ctx.author.id) in jdata['admin']:
            if self.ever_day_48763.is_running():
                self.ever_day_48763.stop()
                await ctx.send('迴圈終止')
            else:
                await ctx.send('尚未啟動')
        else:
            await ctx.send('你沒有權限！')

    @tasks.loop()
    async def ever_day_48763(self):
        self.now = datetime.datetime.now().strftime('%H:%M:%S')

        if self.now == "13:32:43" and self.used == False:
            self.used = True
            for channel_id in self.channels:
                channel = self.bot.get_channel(channel_id)
                print (channel)
                await channel.send('現在是今天的48763秒！你被星爆了！')

        if self.now != "13:32:43" and self.used == True:
            self.used = False



def setup(bot):
    bot.add_cog(bgtask(bot))