"""
This file contains unit tests for the Blizzard and Character classes
"""
import pytest
import requests
from wow.character import Character
from wow.blizzard import BlizzardAPI


def test_api_connection():
    """
    GET requests to Blizzard API docs and site to check if it is reachable
    """
    request = requests.get("https://develop.battle.net/")
    assert request.status_code == 200
    request = requests.get(
        "https://eu.api.blizzard.com/data/wow/achievement-category/index")
    assert request.status_code == 401


@pytest.fixture(scope="module")
def blizzard():
    """
    Logs fixture to reduce the amount of GET requests to Blizzard API
    """
    return BlizzardAPI()


def test_wow_token_api(blizzard):
    """
    Given the blizzard fixture
    Return non empty dict that contains int
    """
    token = blizzard.api.wow.game_data.get_token_index("eu", "en_GB")

    assert token
    assert isinstance(token, dict)
    assert isinstance(token["price"], int)

# def test_wow_token(blizzard):
#    """
#    Given the blizzard fixture
#    Return the price of wow token as int
#    """
#    tokens = blizzard.wow_token()
#
#    assert tokens
#    assert isinstance(tokens, dict)
#    for region in tokens.keys():
#        assert region in REGIONS


def test_character_info_api(blizzard):
    """
    Given the blizzard fixture
    Return non empty dict that character name
    """
    character = blizzard.api.wow.profile.get_character_profile_summary(
        "eu", "en_GB", "kazzak", "syqu")

    assert character
    assert isinstance(character, dict)
    assert "Syqu" in character["name"]


@pytest.mark.asyncio
async def test_character_info(blizzard):
    """
    Given the blizzard fixture
    Return a Character object and validate it
    """
    character = await blizzard.character_info("syqu", "Burning-Legion", "eu")

    assert character
    assert isinstance(character, Character)
    assert character.name == "Syqu"
    assert character.realm == "Burning Legion"
    assert character.faction == "Horde"
    assert character.race == "Orc"
    assert character.spec
    assert character.char_class == "Warlock"
    assert character.ilvl >= character.eq_ilvl
    assert character.guild
    assert character.covenant
    assert character.covenant
    assert character.ach_points
    assert character.others
