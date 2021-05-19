"""
This file contains unit tests for the Warcraft Logs API
"""
import pytest
import requests
from wow.warcraftlogs import WarcraftlogsAPI


def test_api_connection():
    """
    Do two GET requests to API docs and Warcraftlogs site to check if it is reachable
    """
    request = requests.get("https://www.warcraftlogs.com")
    assert request.status_code == 200
    request = requests.get("https://www.warcraftlogs.com/v1/docs")
    assert request.status_code == 200


@pytest.fixture(scope="module")
def logs():
    """
    Logs fixture to reduce the amount of GET requests to Warcraftlogs
    """
    return WarcraftlogsAPI("21WVgBJ6zkwmxPNF")


def test_get_log_info(logs):
    """
    Given the logs fixture
    Return a non empty dictionary
    """
    info = logs.get_log_info()

    assert info
    assert type(info) == dict


def test_get_title(logs):
    """
    Given the logs fixture
    Return a valid string title
    """
    title = logs.get_title()

    assert title
    assert title == "Mythic 03/5 Farm"


def test_get_characters(logs):
    """
    Given the logs fixture
    Return a list of dicts with every Character
    """
    characters = logs.get_characters()

    assert characters
    assert [type(x) == dict for x in characters]
    assert [x["id"] and x["name"] and x["region"] and x["server"]
            for x in characters]
    assert next(x for x in characters if x["name"] ==
                "Squy" and "Elibear" and "Loafcake" and "Arioni" and "Lilborn")


def test_get_fight(logs):
    """
    Given the logs fixture
    Return a Fight object and validate it
    """
    fight = logs.get_fight(2)

    assert fight
    assert fight.id == 7
    assert fight.boss == 2417
    assert fight.start_time == 1858600
    assert fight.end_time == 2106935
    assert fight.duration == abs(1858600 - 2106935)
    assert fight.name == "Stone Legion Generals"
    assert fight.zoneName == "Castle Nathria"
    assert fight.difficulty == "Mythic"
    assert fight.bossPercentage == "72.49%"
    assert fight.others


def test_get_fights_amount(logs):
    """
    Given the logs fixture
    Return the amount of fights in logs
    """
    fights = logs.get_fights_amount()

    assert fights
    assert fights == 18


def test_get_owner(logs):
    """
    Given the logs fixture
    Return the name of logs owner
    """
    owner = logs.get_owner()

    assert owner
    assert owner == "Syqu22"


def test_get_zone(logs):
    """
    Given the logs fixture
    Return the zone id of logs
    """
    zone = logs.get_zone()

    assert zone
    assert zone == "Castle Nathria"


def test_get_duration(logs):
    """
    Given the logs fixture
    Return a duration of logs that is based on the first and last pull
    """
    duration = logs.get_duration()

    assert duration
    assert duration == 10699851


def test_get_total_duration(logs):
    """
    Given the logs fixture
    Return a duration of logs that comes from the difference of logs start time and end time
    """
    duration = logs.get_total_duration()

    assert duration
    assert duration == 10905831
