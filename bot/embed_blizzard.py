from datetime import datetime
from discord.embeds import Embed
from wow.blizzard import BlizzardAPI
import logging

COLOR = 4433254

_logger = logging.getLogger("discord")


class EmbedBlizzardMessage():
    def create_token(self):
        try:
            embed_message = {
                "title": "Wow EU Token",
                "color": COLOR,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
            }
            embed = Embed.from_dict(embed_message)
            blizzard = BlizzardAPI()

            embed.add_field(
                name="EU", value="{0:,}k gold".format(blizzard.wow_token()))

            return embed
        except:
            _logger.error(f"Token info not found")
            return Embed(title="Wow EU Token", description="Token info not found")

    def create_character(self, args: str):
        try:
            credentials = args[0].split("-")
            character = BlizzardAPI().character_info(
                credentials[0], credentials[1])
            embed_message = {
                "title": credentials,
                "color": COLOR,
                "footer": {
                    "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                },
            }
            embed = Embed.from_dict(embed_message)

            embed.add_field(
                name="Name", value=f"{character.char_class}")
            return embed
        except:
            _logger.error(f"Character {credentials} not found")
            return Embed(title="Character", description="Wrong character name or realm")
