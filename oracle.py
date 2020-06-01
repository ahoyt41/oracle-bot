'''
bot.py
'''

import os
import random
import sys
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
        "Owlbear",
        "Goblin",
        "Borpion",
        "Bone faeries",
        "Big Fucking Turtle",
        "Ice Demon",
        "Hogglesnuffer",
        "Rat Goliath",
        "Clay Templar",
        "swarm of bees",
        "swarm of wasps",
        "swarm of swarms",
        "Bat-men",
        "The spirit of the damned"
    ]
desc ={
    "owlbear":"This absolute unit is a massive bear with the crushing beak of an owl. The owlbear will rip you apart if it gets the chance",
    "goblin": "A little green man. He wants gold and is not afraid to commit crimes. \
They usually travel together. ",
    "borpion":"The unholy spawn of a boar and a scorpion, but also massive. \
It is extremely protective of its young and possesses large claws and a stinger full of venom. \
A single sting is often not lethal, but it is certainly unpleasant.",
    "bone faery": "The larger and more aggressive cousin of the well-known and docile tooth fairy. \
It really wants your bones.",
    "big fucking Ttrtle": "Its just a big fucking turtle",
    "ice demon": "A demon made of ice. It has the capacity to freeze things \
and make weapons out of ice using the water in the air. This demon is \
weakened by heat and is especially powerless in hot, dry air.",
    "hogglesnuffer": "Kat Berger came up with this one, ask her.",
    "rat goliath": "A super buff rat mutant; he is also hung like a horse. \
He is super aggressive but will likely run away before fighting to the death. ",
    "merchant":"He has wares if you have coin.",
    "vagabond":"A wanderer. Each one is different. ",
    "orc":"A big, stinky, muscled humanoid. Be careful, \
for he is filled with rage and bloodlust. Approach with caution.",
    "bog witch": "Not to be confused with a sandwich. A woman of the swamps. \
She can communicate with frogs and other such creatures and cast spells. \
She is attuned with nature, though her odor is off-putting." ,
    "clay templar":"A large, humanoid creature carrying a shield and mace, \
typically created by sorcerers. Can reform itself using nearby sources of \
stone. Has a weak spot hidden in its body.",
    "bat-men":"A cross between humans and bats, with large wings and ears, \
they hunt in packs of up to 5. They are virtually blind and find prey \
solely through echolocation. No robins in sight.",
    "swarm of bees": "They’re just bees. Leave them alone.",
    "swarm of wasps": "easily confused with swarm of bees. \
you can easily tell them apart because FUCKFUCKFUCKFUCKFUC",
"swarm of swarms":"It’s a swarm. Of swarms.",
"the spirit of the damned": "A tormented soul sent to the underworld \
who managed to break free. These spirits gain supernatural powers on their \
return to Earth: in exchange, they remain burned by the fires of Hell, \
no matter how cold it may be. This specific type of ghost is incredibly \
rare to find, considering the odds of a soul getting out of Hell in the first place"
    }
encounters = [
    "merchant",
    "vagabond",
    "orc",
    "goblin",
    "bog witch",
    "traveling medic",
    "fountain of \*instert liquid\*",
    "vampire hunter",
    "group of bandits",
    "mysterious cave",
    "necromancer ritual",
    "wounded dragon",
    "boarpion rodeo",
    "thief ambush"

]


#load environment variables from .env
load_dotenv()
#load environment variables into local variables
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
#connect to discord backend
bot = commands.Bot(command_prefix="?")

@bot.command(name="who", help="Choose a random member of the party")
async def who(ctx):
    members = ctx.guild.members
    users = []
    for member in members:
        if not member.bot:
            users.append(member.display_name)
    ndx = int(random.random()*len(users))
    sys.stdout.write("Users = " + str(users)+'\n')
    user = users[ndx]
    sys.stdout.write(user + " is selected\n")
    sys.stdout.flush()
    await ctx.send(user)

@bot.command(name="roll", help="Roll a d20")
async def roll(ctx):    
    roll = (int)((random.random()*20) + 1)
    await ctx.send(ctx.author.display_name + " rolled a " + (str)(roll))


@bot.command(name="swear", help="Insult the user")
async def fuck(ctx):
    ndx = (int)(random.random()*len(swears))
    user = ctx.author.display_name
    await ctx.send(swears[ndx])

@bot.command(name="monster", help="Summon a random monster")
async def monster(ctx):
    ndx = (int)(random.random()*len(monsters))
    await ctx.send("A wild " + monsters[ndx] + " has appeared!!!")

@bot.command(name="describe", help="Describe the specified entity")
async def describe(ctx, *args):
    sys.stdout.writelines("Args is "+ str(len(args)) + " long\n")
    sys.stdout.flush()
    entity = " ".join(args).lower()
    if entity in desc:
        await ctx.send(desc[entity])
    else:
        await ctx.send(entity + " is not found")


@bot.command(name="encounter", help="Randomly spawn an encounter")
async def encounter(ctx):
    ndx = (int)(random.random()*len(encounters))
    await ctx.send("A wild "+ encounters[ndx] + " has appeared!!!")


bot.run(TOKEN)