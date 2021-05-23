from bot.embed_blizzard import EmbedBlizzardMessage
import discord
from discord.ext import commands
import logging

from bot.embed_logs import EmbedLogsMesage
from bot.embed_affixes import EmbedAffixesMessage
from bot.embed_blizzard import EmbedBlizzardMessage

ACTIVITY_MESSAGE = "?help - Bot"
DESCRIPTION = "Example bot help me"
COMMAND_PREFIX = "?"

# Set up logger
_logger = logging.getLogger("discord")
handler = logging.FileHandler(
    filename="logs/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
_logger.addHandler(handler)

# Create bot
bot = commands.Bot(activity=discord.Game(
    ACTIVITY_MESSAGE), command_prefix=COMMAND_PREFIX, description=DESCRIPTION)


def get_token():
    """
    Get private discord token from file
    """
    with open("token.txt", "r") as f:
        return f.readline().strip()


@bot.event
async def on_ready():
    _logger.info(f"Bot logged in as {bot.user}")
    print(f"Bot logged in as {bot.user}")


@bot.event
async def on_message(message):
    """
    Handle warcraftlogs link
    """
    url_prefix = "https://www.warcraftlogs.com/reports/"

    if message.content.startswith(url_prefix):
        await message.channel.send(embed=EmbedLogsMesage(url=message.content).create())
    else:
        await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!")


@bot.command()
async def affixes(ctx, *args):
    await ctx.send(embed=EmbedAffixesMessage(args).create())


@bot.command()
async def token(ctx):
    await ctx.send(embed=EmbedBlizzardMessage().create_token())


@bot.command()
async def character(ctx, *args):
    await ctx.send(embed=EmbedBlizzardMessage().create_character(args))
