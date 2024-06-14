# import the modules we need
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# load the environment variables
load_dotenv()

# create a bot instance
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# We have used commands.Bot instead of discord.Bot as we want to use prefixed commands
# We have also passed the intents parameter to the bot instance to enable all intents
# This is required to use certain features like member join, leave, etc.


# event listener for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


# prefix command with the bot instance
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')


if __name__ == '__main__':  # this is known as a run guard to prevent the bot from running when the file is imported
    # run the bot with the token from the .env file
    bot.run(os.getenv('DISCORD_TOKEN'))
