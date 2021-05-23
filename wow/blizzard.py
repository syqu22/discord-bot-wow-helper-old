from wow.character import Character
from blizzardapi import BlizzardApi

CLIENT_ID = "a30c40f5dba24d53bff5201464f92e8d"
REGION = "eu"
LOCALE = "en_GB"


class BlizzardAPI():

    def __init__(self):
        self.api = BlizzardApi(CLIENT_ID, self.get_secret())

    def get_secret(self):
        with open("secret.txt") as f:
            return f.readline().strip()

    def wow_token(self):
        try:
            api = self.api.wow.game_data.get_token_index(REGION, LOCALE)
            price = api["price"] / 10000

            return int(price)
        except:
            return None

    def character_info(self, name: str, realm: str):
        try:
            api = self.api.wow.profile
            character = api.get_character_profile_summary(
                REGION, LOCALE, realm.lower(), name.lower())

            return Character(**character)
        except:
            return None

    def character_avatar(self, name: str, realm: str):
        try:
            api = self.api.wow.profile
            avatar = api.get_character_media_summary(
                REGION, LOCALE, realm.lower(), name.lower())

            return avatar["assets"][1]["value"]
        except:
            return None
