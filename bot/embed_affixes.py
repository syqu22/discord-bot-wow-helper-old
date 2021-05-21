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
                            value=affixes.affixes_from_week()(num))

            return embed

        else:
            embed.add_field(name="Previous Week Affixes",
                            value=affixes.previous_affixes())
            embed.add_field(name="Current Week Affixes",
                            value=affixes.current_affixes())
            embed.add_field(name="Next Week Affixes",
                            value=affixes.next_affixes()())

            return embed
