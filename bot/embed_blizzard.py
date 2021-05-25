from datetime import datetime
from discord.embeds import Embed
from wow.blizzard import BlizzardAPI
import logging

_logger = logging.getLogger("discord")


class EmbedBlizzardMessage():
    def create_token(self):
        try:
            blizzard = BlizzardAPI()
            embed_message = {
                "title": "WoW Tokens",
                "color": 4433254,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
            }
            embed = Embed.from_dict(embed_message)
            tokens = blizzard.get_wow_token_prices()
            for region, price in tokens.items():
                embed.add_field(
                    name=region.upper(), value="**{0:,}k** Gold".format(int(price)))

            return embed
        except:
            _logger.error(f"Token info not found")
            return Embed(title="WoW Token", description="Token info not found")

    def create_character(self, name_realm: str):
        try:
            # credentials[0] = Name, credentials[1] = Realm
            credentials = name_realm.split("-", 1)
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
                name="Links", value=f"[Raider.IO](https://raider.io/characters/eu/{credentials[1]}/{credentials[0]}) | "
                "[WarcraftLogs](https://www.warcraftlogs.com/character/eu/{credentials[1]}/{credentials[0]}) | "
                "[WoWProgress](https://www.wowprogress.com/character/eu/{credentials[1]}/{credentials[0]})"
            )
            embed.add_field(
                name="Covenant", value=f"{character.covenant}",
            )
            embed.add_field(
                name="Achievements", value=f"[{character.ach_points}]({armory_url + 'achievements'})"
            )

            return embed
        except:
            _logger.error(f"Character search for {credentials} returned error")
            return Embed(title="Character", description="Wrong character name or realm")
