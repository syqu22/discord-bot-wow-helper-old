from datetime import datetime
from discord.embeds import Embed
from wow.affixes import Affixes

COLOR = 2075661


class EmbedAffixesMessage():
    def __init__(self, args):
        self.args = args

    def create(self):
        embed_message = {
            "title": "Affixes",
            "color": COLOR,
            "footer": {
                "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
        }
        embed = Embed.from_dict(embed_message)
        affixes = Affixes()

        if self.args and self.args[0].isnumeric():
            num = int(self.args[0])
            embed.add_field(name=f"Week {num} affixes",
                            value=affixes.affixesFromWeek(num))

            return embed

        else:
            embed.add_field(name="Previous Week Affixes",
                            value=affixes.previousWeekAfixes())
            embed.add_field(name="Current Week Affixes",
                            value=affixes.currentAffixes())
            embed.add_field(name="Next Week Affixes",
                            value=affixes.nextWeekAffixes())

            return embed
