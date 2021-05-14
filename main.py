from warcraftlogs import WarcraftlogsAPI
import discord
import logging
from datetime import datetime

URL_PREFIX ="https://www.warcraftlogs.com/reports/"

#Set up logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

def get_token():
    with open("token.txt", "r") as f:
        return f.readline().strip()

@client.event
async def on_ready():
    logger.info("Bot logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #DELETE LATER
    messages = await message.channel.history().flatten()
    if message.content.startswith("clear"):
        await message.channel.delete_messages(messages)
        await message.channel.send(f"{message.author.mention} wlasnie rozjebal wszystkie wiadomosci xD", delete_after=10)

    #DELETE LATER
    if message.content.startswith("task"):
        task_id = 0
        async for _ in message.channel.history():
            task_id += 1

        await message.delete()
        msg = await message.channel.send(embed=discord.Embed(title=f"Task {task_id}", description=message.content[4:]))
        await msg.add_reaction(u"👍")

    if message.content.startswith(URL_PREFIX):
        warcraftlogs_url = message.content
        await message.channel.send(embed=create_warcraftlogs_embed(url=warcraftlogs_url))

#DELETE LATER
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.emoji == u"👍":
        await reaction.message.delete()

def create_warcraftlogs_embed(url: str):
    code = url[len(URL_PREFIX):]
    time = datetime.now()

    test_embed = {
        "title": "Bot",
        "description": "Test description",
        "url": url,
        "color": 15,
        "footer": {
            "text": time
        },
        "thumbnail": {
            "url": url
        },
        "author": {
            "name": "Bot maciek",
        },
        "fields": [{
            "name": "Bot maciek",
            "value": "bot andrzej"
        },{
            "name": "Bot maciek",
            "value": "bot andrzej" 
        },{
            "name": "Bot maciek",
            "value": "bot andrzej" 
        }]
    }

    return discord.Embed.from_dict(data=test_embed)

if __name__ == "__main__":
    client.run(get_token())
