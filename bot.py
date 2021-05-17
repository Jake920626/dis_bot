import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='yu')

@bot.event
async def on_ready():
    print(">> bot is ready <<")

bot.run('ODQzNzA0MzY1NzI5NDQ3OTc3.YKHu7A.4Wt__c5eX-04yJGLqyXE0viPtKg')