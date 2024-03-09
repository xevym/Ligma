import discord
from discord.ext import commands
import random
import os

print(os.listdir('images'))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def trash(ctx):
    text_name = os.listdir('titles')
    abc = random.choice(text_name)
    with open(f'titles/{abc}', 'r') as f:
        await ctx.send(f.read())

bot.run('TOKEN')

#make a folder named titles
