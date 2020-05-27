'''
bot.py
'''

import os
import random
from dotenv import load_dotenv
from discord.ext import commands

swears = [
        "Fuck",
        "Shit",
        "Bitch ass",
        "Curses",
        "Jesus Fucking Christ",
        "Christ on a bike",
        "Ballsack",
        "Suck my left nut",
        "You're stinky"
    ]
monsters = [
        "owlbear",
        "goblin",
        "borpian",
        "bone fairies",
        "big fucking turtle"
    ]

#load environment variables from .env
load_dotenv()
#load environment variables into local variables
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
#connect to discord backend
bot = commands.Bot(command_prefix="?")

@bot.command(name="roll", help="roll a d20")
async def roll(ctx):    
    roll = (int)((random.random()*20) + 1)
    await ctx.send(ctx.author.display_name + " rolled a " + (str)(roll))


@bot.command(name="swear")
async def fuck(ctx):
    ndx = (int)(random.random()*len(swears))
    user = ctx.author.display_name
    await ctx.send(swears[ndx])

@bot.command(name="monster")
async def monster(ctx):
    ndx = (int)(random.random()*len(monsters))
    await ctx.send(monsters[ndx])


bot.run(TOKEN)