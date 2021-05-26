from datetime import datetime
from discord.embeds import Embed
from wow.blizzard import BlizzardAPI
import logging

_logger = logging.getLogger("discord")


class EmbedBlizzardMessage():
    async def create_token(self):
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
            tokens = await blizzard.get_wow_token_prices()
            for region, price in tokens.items():
                embed.add_field(
                    name=region.upper(), value="**{0:,}k** Gold".format(int(price)))

            return embed
        except:
            _logger.error(f"Token info not found")
            return Embed(title="WoW Token", description="Token info not found")

    async def create_character(self, name_realm: str, region: str):
        try:
            api = BlizzardAPI()
            # credentials[0] = Name, credentials[1] = Realm
            credentials = name_realm.split("-", 1)
            character = await api.character_info(
                credentials[0], credentials[1], region)
            armory_url = f"https://worldofwarcraft.com/en-gb/character/{region}/{credentials[1]}/{credentials[0]}/"

            embed_message = {
                "title": f"({character.level}) {character.name}-{character.realm} <{character.guild}>",
                "url": armory_url,
                "color": 4433254,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
                "image": {
                    "url": await api.character_avatar(credentials[0], credentials[1], region)
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
                name="Links", value=f"[Raider.IO](https://raider.io/characters/{region}/{credentials[1]}/{credentials[0]}) | "
                "[WarcraftLogs](https://www.warcraftlogs.com/character/{region}/{credentials[1]}/{credentials[0]}) | "
                "[WoWProgress](https://www.wowprogress.com/character/{region}/{credentials[1]}/{credentials[0]})"
            )
            embed.add_field(
                name="Covenant", value=f"{character.covenant}",
            )
            embed.add_field(
                name="Achievements", value=f"[{character.ach_points}]({armory_url + 'achievements'})"
            )

            return embed
        except:
            _logger.error(
                f"Character {credentials} with region {region} returned error")
            return Embed(title="Character", description="Wrong character name, realm or region. Remember to put "
                         "region after name-realm if the character is not on EU realm.")
