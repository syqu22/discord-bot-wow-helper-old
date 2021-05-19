from datetime import datetime
from discord.embeds import Embed
from wow.warcraftlogs import WarcraftlogsAPI

COLOR = 9066993


class EmbedLogsMesage():
    def __init__(self, url: str):
        self.url = url
        self.code = url[37:53]

    def create(self):
        code = WarcraftlogsAPI(self.code)
        # Check if logs zone is not from raid
        if not code.get_zone():
            embed = Embed(title="Unsupported Zone",
                          description="We are very sorry but our bot is currently not supporting anything else except raids.")
            embed.set_footer(text=datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
            return embed
        else:

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


def zone_image(logs: WarcraftlogsAPI):
    CN = "https://i.imgur.com/alf87cE.jpg"
    SOD = "https://i.imgur.com/rmSPyDG.jpg"

    if logs.get_zone() == "Castle Nathria":
        return CN
    elif logs.get_zone() == "Sanctum of Domination":
        return SOD
    else:
        return ""
