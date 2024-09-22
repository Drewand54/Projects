import nextcord
import config
import os
import json
import requests
from nextcord.ext import commands

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('_____________________________________________')




#Load Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')













bot.run(config.TOKEN)
