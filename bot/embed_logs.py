from datetime import datetime
from discord.embeds import Embed
from wow.warcraftlogs import WarcraftlogsAPI
import logging

COLOR = 9066993

_logger = logging.getLogger("discord")


class EmbedLogsMesage():
    def __init__(self, url: str):
        self.url = url
        self.code = url[37:53]

    def create(self):
        code = WarcraftlogsAPI(self.code)
        try:

            embed_message = {
                "title": f"{code.get_title()} - {datetime.fromtimestamp(code.get_total_duration()/1000.0).strftime('%H:%M:%S')} ",
                "url": self.url,
                "color": COLOR,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
                "image": {
                    "url": zone_image(code)
                }
            }

            embed = Embed.from_dict(embed_message)

            for i in range(code.get_fights_amount()):
                fight = code.get_fight(i)
                embed.add_field(name=f"{i+1}. {fight.name} ({fight.difficulty})",
                                value=f"{fight.bossPercentage} | {datetime.fromtimestamp(fight.duration/1000.0).strftime('%M:%S')} | [Link](https://www.warcraftlogs.com/reports/{self.code}#fight={fight.id})",
                                inline=True)

            return embed
        except:
            _logger.error(f"Log with url {self.url} returned error")
            return Embed(title="Log error",
                         description="Make sure the link is correct (remember that bot currently does not support Mythic+ and Torghast")


def zone_image(logs: WarcraftlogsAPI):
    CN = "https://i.imgur.com/alf87cE.jpg"
    SOD = "https://i.imgur.com/rmSPyDG.jpg"

    if logs.get_zone() == "Castle Nathria":
        return CN
    elif logs.get_zone() == "Sanctum of Domination":
        return SOD
    else:
        return ""
