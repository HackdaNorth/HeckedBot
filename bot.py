# bot.py
import os
import discord
import progress
import random
from discord.ext import commands

from progress.bar import Bar

def pickAGame():
    playableGames = ["GTA V","Rocket League","Halo Reach (Mulitplayer)",
                "Halo 2", "Halo 1", "Gunfire Reborn", "Rust", 'Among Us',
                "Left 4 Dead 2", "Killing Floor 2", "SpyParty", "Witch It",
                "CSGO", "HELLDIVERS","Awesomenauts","Plague Inc: Evolved",
                "Dungeon of the Endless", "Shell Shock", "Rainbow Six Siege",
                "Insurgency", "Risk Of Rain 2", "Astroneer", "Roguelands",
                "Move Or Die", "Towner Unite", "TANKNAROK", "Table Sim",
                "Phasmophobia", "Project Winter", "GREEN HELL", "Unrailed!",
                "Raft", "Brawlhalla", "Deep Rock Galactic", "7 Ways to Die",
                "Iron Harvest", "Call of Duty", "Star wars: Squadron",
                "Star wars: Battlefront","Overwatch", "Satisfactory",
                "Gang Beasts", "Minecraft", "Portal 2", "Payday 2",
                "Trine 2", "CUPHEAD", "Diablo 3", " Don't starve together",
                "GTFO"]
    amountOfGames = len(playableGames)
    randomInt = random.randint(0, amountOfGames)
    gamePicked = playableGames[randomInt]
    return gamePicked

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='#', description=description, intents=intents)


@bot.event

async def on_ready():
bar = Bar('Starting', max=20, fill='@',suffix='%(percent)d%%', avg='20')
    for i in range(20):
        bar.next()
        print('\n' + 'Logged in as USER:', self.user)
        bar.next()
        print('USER_ID:', self.user.id)
        bar.next()
        print('\n' + 'Waiting for Message.....')
        bar.next()
    bar.finish();
@bot.command()
async def stream(ctx, left: int, right: int):
    """Start Stream Presence"""
    print('Presence Switch initiated')
    await client.change_presence(activity=discord.Streaming(name="Robin Adventures", url="xxx"))

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def chooseGame(ctx, *choices: str):
    """Chooses between multiple choices."""
    print('Game Picking initiated')
    await message.channel.send(pickAGame())

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.event
async def on_message(self, message):
    #record all messages seen
    print('\n' + 'MESSAGED RECEIVED FROM USER: ' + 
        message.author.name + ' ----' +
        'MESSGAE CONTENT: ' + message.content)
        #don't respond to itself
        if message.author.name == self.user:
            return

bot.run('xxxx')