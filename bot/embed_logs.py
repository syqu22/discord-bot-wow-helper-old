from datetime import datetime

from discord.embeds import Embed
from wow.warcraftlogs import WarcraftlogsAPI


class EmbedLogsMesage():
    def __init__(self, url: str):
        self.url = url
        self.code = url[37:53]

    async def create(self):
        try:
            code = await WarcraftlogsAPI(self.code)
            embed_message = {
                "title": f"{await code.get_title()} - {datetime.fromtimestamp(await code.get_total_duration()/1000.0).strftime('%H:%M:%S')} ",
                "url": self.url,
                "color": 9066993,
                "image": {
                    "url": await zone_image(code)
                }
            }
            embed = Embed.from_dict(embed_message)

            for i in range(await code.get_fights_amount()):
                fight = await code.get_fight(i)
                embed.add_field(name=f"{i+1}. {fight.name} ({fight.difficulty})",
                                value=f"[Link](https://www.warcraftlogs.com/reports/{self.code}#fight={fight.id}) | {datetime.fromtimestamp(fight.duration/1000.0).strftime('%M:%S')} | {fight.bossPercentage}",
                                inline=True)

            return embed
        except:
            print(f"Log with url {self.url} returned error")

            return Embed(title="Log error",
                         description="Wrong link or logs are set to private.")


async def zone_image(logs: WarcraftlogsAPI):
    zone = await logs.get_zone()

    if zone == "Mythic+":
        return "https://i.imgur.com/VT7yTYl.jpg"
    elif zone == "Castle Nathria":
        return "https://i.imgur.com/cssCW3A.jpg"
    elif zone == "Torghast":
        return "https://i.imgur.com/a3Kzwws.jpg"
    elif zone == "Sanctum of Domination":
        return "https://i.imgur.com/X5Kk2JO.jpg"
    else:
        return ""
