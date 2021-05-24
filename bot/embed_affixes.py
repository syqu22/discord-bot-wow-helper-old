from datetime import datetime
from discord.embeds import Embed
from wow.affixes import Affixes
import logging

_logger = logging.getLogger("discord")


class EmbedAffixesMessage():
    def create(self, week: int):
        try:
            affixes = Affixes()
            embed_message = {
                "title": "Affixes",
                "color": 2075661,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
            }
            embed = Embed.from_dict(embed_message)
            if week:
                num = int(week)
                embed.add_field(name=f"Week {num} Affixes",
                                value=affixes.affixes_from_week(num))

                return embed
            else:
                embed.add_field(name=f"Previous Week {affixes.weeks_since_launch-1} Affixes",
                                value=affixes.previous_affixes())
                embed.add_field(name=f"Current Week {affixes.weeks_since_launch} Affixes",
                                value=affixes.current_affixes())
                embed.add_field(name=f"Next Week {affixes.weeks_since_launch+1}Affixes",
                                value=affixes.next_affixes())

                return embed
        except:
            _logger.error(
                f"Affixes command with additional parameters {week} returned error")
            return Embed(title="Wrong week", description="Make sure given week is smaller than 100 and the command is correct \n Example: ?affixes <week>")
