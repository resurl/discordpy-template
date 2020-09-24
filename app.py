import os
import discord
import loadconfig
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!')

# runs once on ready
@bot.event
async def on_ready():
    print(f'Bot name: {bot.user.name}')
    print(f'Discord version: {discord.__version__}')
    # loads all cogs specified in config/cogs.py
    for cog in loadconfig.__cogs__:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f'Unable to load cog: {cog}, {e}')

# example chat command function definition
@bot.command(aliases=['hi','hello'])
async def hello(ctx):
    await ctx.send(f'hello {ctx.author.mention}')

bot.run(TOKEN)