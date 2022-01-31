import discord
from discord.ext import commands , tasks
import json
import random
import os,datetime

import core.classinit
from core.load import load

jdata = {}

jdata = load('text')

"""
此類別為背景作業類別，用來進行在背景的回圈作業
"""
class bgtask (core.classinit.Cog_Extension):

    def __init__(self,bot):
        super().__init__(bot)
        print(jdata)
        self.channels = jdata['channels']
        self.now = datetime.datetime.now().strftime('%H:%M:%S')
        self.used = False
        self.loop_running = jdata['loop_running']

        if self.loop_running == 1:
            self.ever_day_48763.start()

    @commands.command()
    async def set_channel(self,ctx):
        global jdata
        if str(ctx.author.id) in jdata['admin']:
            if ctx.channel.id not in self.channels: 
                self.channels.append(ctx.channel.id) 
                channels_updates = {'channels':self.channels,'loop_running':self.loop_running}
                with open('text/channels.json','w')as updates:
                    json.dump(channels_updates,updates)
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
                self.loop_running = 1
                channels_updates = {'channels':self.channels,'loop_running':self.loop_running}
                with open('text/channels.json','w')as updates:
                    json.dump(channels_updates,updates)
                await ctx.send('迴圈開始')
        else:
            await ctx.send('你沒有權限！')

    @commands.command()
    async def stop_loop(self,ctx):
        if str(ctx.author.id) in jdata['admin']:
            if self.ever_day_48763.is_running():
                self.ever_day_48763.stop()
                self.loop_running = 0
                channels_updates = {'channels':self.channels,'loop_running':self.loop_running}
                with open('text/channels.json','w')as updates:
                    json.dump(channels_updates,updates)
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