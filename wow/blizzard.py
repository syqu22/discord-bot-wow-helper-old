import os
from wow.character import Character
from blizzardapi import BlizzardApi
from discord.ext import tasks
import logging

_logger = logging.getLogger("discord")

REGIONS = ["eu", "us", "kr", "tw", "cn"]
LOCALE = "en_GB"

token_prices = dict()


class BlizzardAPI():
    def __init__(self):
        self.api = BlizzardApi(os.getenv("BLIZZARD_CLIENT"),
                               os.getenv("BLIZZARD_SECRET"))

    @tasks.loop(seconds=1800.0)
    async def fetch_wow_token_prices(self):
        """
        Fetch wow token prices every 30min
        """
        try:
            api = self.api.wow.game_data
            for region in REGIONS:
                token_prices[region] = int(api.get_token_index(
                    region, LOCALE)["price"]) / 10000

            _logger.info("Succesfully fetched WoW token prices data")
        except:
            _logger.error(
                "There was an error during fetching WoW token prices data")
            return None

    async def get_wow_token_prices(self):
        """
        Return the price `int` of the EU WoW token
        """
        return token_prices

    async def character_info(self, name: str, realm: str, region: str):
        """
        Return the `Character` object from Blizzard API `dict`
        """
        try:
            api = self.api.wow.profile

            # If given region is not correct or not set,, use default EU
            if region not in REGIONS:
                region = REGIONS[0]

            character = api.get_character_profile_summary(
                region, LOCALE, realm.lower(), name.lower())

            return Character(**character)
        except:
            _logger.error(
                f"There was an error while getting character info with {name}-{realm} credentials and region {region}")
            return None

    async def character_avatar(self, name: str, realm: str, region: str):
        """
        Return the url `str` to the picture of character
        """
        try:
            # If given region is not correct or not set, use default EU
            if region not in REGIONS:
                region = REGIONS[0]
            api = self.api.wow.profile
            avatar = api.get_character_media_summary(
                region, LOCALE, realm.lower(), name.lower())

            return avatar["assets"][1]["value"]
        except:
            _logger.error(
                f"There was an error while getting character avatar for {name}-{realm}")
            return None
