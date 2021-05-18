from datetime import datetime
from discord.embeds import Embed
from warcraftlogs import WarcraftlogsAPI

DESCRIPTION = "Beep boob bop imam robot"
COLOR = 3066993
IMAGE_URL = "https://data1.cupsell.pl/upload/generator/10838/640x420/229559_print-trimmed-1.png?resize=max_sizes&key=55f9a22768eed085006592c1174c0235"


class EmbedLogsMesage():
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url
        self.code = url[37:53]  # TODO FIX

    def create(self):

        embed_message = {
            "title": self.title,
            "description": DESCRIPTION,
            "url": self.url,
            "color": COLOR,
            "footer": {
                "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
            "image": {
                "url": IMAGE_URL
            }
        }

        embed = Embed.from_dict(embed_message)
        code = WarcraftlogsAPI(self.code)

        for i in range(code.get_fights_amount()):
            fight = code.get_fight(i)
            embed.add_field(name=f"{i+1}. {fight.name} ({fight.difficulty})",
                            value=f"Health: {fight.bossPercentage} https://www.warcraftlogs.com/reports/{self.code}#fight={fight.id}",
                            inline=False)

        return embed
