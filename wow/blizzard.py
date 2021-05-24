import os
from wow.character import Character
from blizzardapi import BlizzardApi

REGIONS = ["eu", "us", "kr", "tw", "cn"]
LOCALE = "en_GB"


class BlizzardAPI():
    def __init__(self):
        self.api = BlizzardApi(os.getenv("BLIZZARD_CLIENT"),
                               os.getenv("BLIZZARD_SECRET"))

    def wow_token(self):
        """
        Return the price `int` of the EU WoW token
        """
        try:
            api = self.api.wow.game_data
            token_prices = dict()

            for region in REGIONS:
                token_prices[region] = int(api.get_token_index(
                    region, LOCALE)["price"]) / 10000

            return token_prices
        except:
            return None

    def character_info(self, name: str, realm: str):
        """
        Return the `Character` object from Blizzard API `dict`
        """
        try:
            api = self.api.wow.profile
            character = api.get_character_profile_summary(
                REGIONS[0], LOCALE, realm.lower(), name.lower())

            return Character(**character)
        except:
            return None

    def character_avatar(self, name: str, realm: str):
        """
        Return the url `str` to the picture of character
        """
        try:
            api = self.api.wow.profile
            avatar = api.get_character_media_summary(
                REGIONS[0], LOCALE, realm.lower(), name.lower())

            return avatar["assets"][1]["value"]
        except:
            return None
