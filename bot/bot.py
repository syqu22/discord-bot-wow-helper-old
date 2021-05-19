import discord
from discord.ext import commands
import logging

from bot.embed_logs import EmbedLogsMesage

ACTIVITY_MESSAGE = "?help - Bot"
DESCRIPTION = "Example bot help me"
COMMAND_PREFIX = "?"

# Set up logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename="logs/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

# Create bot
bot = commands.Bot(activity=discord.Game(
    ACTIVITY_MESSAGE), command_prefix=COMMAND_PREFIX, description=DESCRIPTION, help_command=None)


def get_token():
    """
    Get private discord token from file
    """
    with open("token.txt", "r") as f:
        return f.readline().strip()


@bot.event
async def on_ready():
    logger.info(f"Bot logged in as {bot.user}")
    print(f"Bot logged in as {bot.user}")


@bot.event
async def on_message(message):
    """
    Handle warcraftlogs link
    """
    url_prefix = "https://www.warcraftlogs.com/reports/"

    if message.content.startswith(url_prefix):
        await message.channel.send(embed=EmbedLogsMesage(url=message.content).create())
        # await msg.add_reaction(u"✅")
        # await msg.add_reaction(u"❎")
        # await msg.add_reaction(u"📧")
    else:
        await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f"pong")


@bot.command()
async def affix(ctx):
    await ctx.send(f"")


@bot.command()
async def help(ctx):
    await ctx.send(", ".join(str(i) for i in bot.commands))
