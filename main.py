from warcraftlogs import WarcraftlogsAPI
import discord
import logging
from datetime import datetime

URL_PREFIX ="https://www.warcraftlogs.com/reports/"

#Set up logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

client = discord.Client()

#Get private discord token from file
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

    if message.content.startswith(URL_PREFIX):
        msg = await message.channel.send(embed=create_warcraftlogs_embed(url=message.content))
        await msg.add_reaction(u"✅")
        await msg.add_reaction(u"❎")
        await msg.add_reaction(u"📧")
        
def create_warcraftlogs_embed(url: str):
    code = url[len(URL_PREFIX):]
    #logs = WarcraftlogsAPI(code)

    test_embed = {
        "title": "Bot",
        "description": "Test description",
        "url": url,
        "color": 15,
        "footer": {
            "text": str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
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
