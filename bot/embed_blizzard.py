from datetime import datetime
from discord.embeds import Embed
from wow.blizzard import BlizzardAPI
import logging

_logger = logging.getLogger("discord")


class EmbedBlizzardMessage():
    def create_token(self):
        try:
            embed_message = {
                "title": "Wow EU Token",
                "color": 4433254,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
            }
            embed = Embed.from_dict(embed_message)
            blizzard = BlizzardAPI()
            embed.add_field(
                name="EU", value="**{0:,}k** Gold".format(blizzard.wow_token()))

            return embed
        except:
            _logger.error(f"Token info not found")
            return Embed(title="Wow EU Token", description="Token info not found")

    def create_character(self, args: str):
        try:
            # credentials[0] = Name, credentials[1] = Realm
            credentials = args[0].split("-", 1)
            character = BlizzardAPI().character_info(
                credentials[0], credentials[1])
            armory_url = f"https://worldofwarcraft.com/en-gb/character/eu/{credentials[1]}/{credentials[0]}/"

            embed_message = {
                "title": f"({character.level}) {character.name}-{character.realm} <{character.guild}>",
                "url": armory_url,
                "color": 4433254,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
                "image": {
                    "url": BlizzardAPI().character_avatar(credentials[0], credentials[1])
                }
            }
            embed = Embed.from_dict(embed_message)
            embed.add_field(
                name="Spec", value=f"{character.race} {character.spec} {character.char_class}")
            embed.add_field(
                name="Faction", value=f"{character.faction}"
            )
            embed.add_field(
                name="Item level", value=f"({character.ilvl}) {character.eq_ilvl}"
            )
            embed.add_field(
                name="Achievements", value=f"[{character.ach_points}]({armory_url + 'achievements'}) points"
            )
            embed.add_field(
                name="Covenant", value=f"{character.covenant}"
            )
            embed.add_field(
                name="Links", value=f"[Raider.IO](https://raider.io/characters/eu/{credentials[1]}/{credentials[0]}) | "
                "[WarcraftLogs](https://www.warcraftlogs.com/character/eu/{credentials[1]}/{credentials[0]}) | "
                "[WowProgress](https://www.wowprogress.com/character/eu/{credentials[1]}/{credentials[0]})"
            )

            return embed
        except:
            _logger.error(f"Character search of {credentials} returned error")
            return Embed(title="Character", description="Wrong character name or realm")
