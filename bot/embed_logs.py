from datetime import datetime
from discord.embeds import Embed
from wow.warcraftlogs import WarcraftlogsAPI
import logging

_logger = logging.getLogger("discord")


class EmbedLogsMesage():
    def __init__(self, url: str):
        self.url = url
        self.code = url[37:53]

    def create(self):
        try:
            code = WarcraftlogsAPI(self.code)
            embed_message = {
                "title": f"{code.get_title()} - {datetime.fromtimestamp(code.get_total_duration()/1000.0).strftime('%H:%M:%S')} ",
                "url": self.url,
                "color": 9066993,
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
                                value=f"[Link](https://www.warcraftlogs.com/reports/{self.code}#fight={fight.id}) | {datetime.fromtimestamp(fight.duration/1000.0).strftime('%M:%S')} | {fight.bossPercentage}",
                                inline=True)

            return embed
        except:
            _logger.error(f"Log with url {self.url} returned error")
            return Embed(title="Log error",
                         description="Wrong link to logs")


def zone_image(logs: WarcraftlogsAPI):
    if logs.get_zone() == "Mythic+":
        return "https://i.imgur.com/VT7yTYl.jpg"
    elif logs.get_zone() == "Castle Nathria":
        return "https://i.imgur.com/cssCW3A.jpg"
    elif logs.get_zone() == "Torghast":
        return "https://i.imgur.com/a3Kzwws.jpg"
    elif logs.get_zone() == "Sanctum of Domination":
        return "https://i.imgur.com/X5Kk2JO.jpg"
    else:
        return ""
