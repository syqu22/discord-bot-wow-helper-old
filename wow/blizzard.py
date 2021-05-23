import os
from wow.character import Character
from blizzardapi import BlizzardApi

REGION = "eu"
LOCALE = "en_GB"


class BlizzardAPI():
    def __init__(self):
        self.api = BlizzardApi(os.getenv("BLIZZARD_CLIENT"),
                               os.getenv("BLIZZARD_SECRET"))

    def wow_token(self):
        """
        Return the price `int` of the EU Wow token
        """
        try:
            api = self.api.wow.game_data.get_token_index(REGION, LOCALE)
            price = api["price"] / 10000

            return int(price)
        except:
            return None

    def character_info(self, name: str, realm: str):
        """
        Return the `Character` object from Blizzard API `dict`
        """
        try:
            api = self.api.wow.profile
            character = api.get_character_profile_summary(
                REGION, LOCALE, realm.lower(), name.lower())

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
                REGION, LOCALE, realm.lower(), name.lower())

            return avatar["assets"][1]["value"]
        except:
            return None
