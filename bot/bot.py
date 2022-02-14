import discord
from discord.ext import commands
from wow.blizzard import BlizzardAPI

from bot.embed_affixes import EmbedAffixesMessage
from bot.embed_blizzard import EmbedBlizzardMessage
from bot.embed_logs import EmbedLogsMesage

ACTIVITY_MESSAGE = "v2 update soon!"
COMMAND_PREFIX = "?"

# Create bot
bot = commands.Bot(activity=discord.Game(
    ACTIVITY_MESSAGE), command_prefix=COMMAND_PREFIX)


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    # Start fetching wowtoken data task
    await BlizzardAPI().fetch_wow_token_prices.start()


@bot.command(description="Pong?")
async def ping(ctx):
    await ctx.channel.send(f"Pong!")


@bot.command(brief="Shows fights from WarcraftLogs log", description="Shows fights from WarcraftLogs log as a list with clickable link to each fight. It's also showing the health of boss, "
             "combat duration. Additionally there's an information about zone.")
async def log(ctx, url: str):
    url_prefix = "https://www.warcraftlogs.com/reports/"
    if url.startswith(url_prefix):
        await ctx.channel.send(embed=await EmbedLogsMesage(url=url).create())


@bot.command(brief="Shows up to date affixes", description="Shows affixes for previous/current/next week. Can also show affixes for the week user wants"
             " by adding additional parameter [week], which will return affixes for that week.")
async def affixes(ctx, week: int = None):
    await ctx.channel.send(embed=await EmbedAffixesMessage().create(week=week))


@bot.command(brief="Shows current price of the WoW token", description="Shows current price of the WoW token, data is taken from EU, US, KR, TW and CN regions.")
async def token(ctx):
    await ctx.channel.send(embed=await EmbedBlizzardMessage().create_token())


@bot.command(brief="Shows information about given character", description="Shows information about given character. Make sure character name and realm"
             "are written correctly in format <name>-<realm> [region] (capitalization is not neccessary). By default region is set to EU, other supported regions are: \nUS, KR, TW, CN. (Use shortcuts for regions)")
async def character(ctx, name_realm: str, region: str = None):
    await ctx.channel.send(embed=await EmbedBlizzardMessage().create_character(name_realm=name_realm, region=region))
