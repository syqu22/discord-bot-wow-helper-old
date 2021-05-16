"""
This file contains unit tests for the Warcraft Logs API
"""
import pytest
from enums import Events, Zones
from warcraftlogs import WarcraftlogsAPI

@pytest.fixture(scope="module")
def logs():
    """
    Logs fixture to reduce the amount of GET requests to Warcraftlogs
    """
    return WarcraftlogsAPI("21WVgBJ6zkwmxPNF")

def test_get_log_info(logs):
    """
    Given the logs code
    Return a non empty dictionary
    """
    info = logs.get_log_info()

    assert info
    assert type(info) == dict

def test_get_title(logs):
    """
    Given the logs code
    Return a valid string title
    """
    title = logs.get_title()

    assert title
    assert title == "Mythic 03/5 Farm"

def test_get_characters(logs):
    """
    Given the logs code
    Return a list of dicts with every Character
    """
    characters = logs.get_characters()

    assert characters
    assert [type(x) == dict for x in characters]
    assert [x["id"] and x["name"] and x["region"] and x["server"] for x in characters]
    assert next(x for x in characters if x["name"] == "Squy" and "Elibear" and "Loafcake" and "Arioni" and "Lilborn")

def test_get_fights(logs):
    """
    Given the logs code
    Return a list of dicts of fights
    """
    fights = logs.get_fights()

    assert type(fights) == list
    assert [x["boss"] and x["id"] and x["name"] and x["bossPercentage"] and x["start_time"] and x["end_time"] and x["difficulty"] for x in fights]
    assert next(x for x in fights if x["name"] == "Sire Denathrius" and "Sludgefist" and "Stone Legion Generals")


def test_get_log_start(logs):
    """
    Given the logs code
    Return an int of logs start in milliseconds
    """
    start = logs.get_log_start()

    assert start
    assert type(start) == int

def test_get_log_end(logs):
    """
    Given the logs code
    Return an int of logs end in milliseconds
    """
    end = logs.get_log_end()

    assert end
    assert type(end) == int


def test_get_log_duration(logs):
    """
    Given the logs code
    Return an duration of logs that comes from the difference of logs start time and end time
    """
    duration = logs.get_log_duration()
    start = logs.get_log_start()
    end = logs.get_log_end()

    assert duration
    assert abs(start - end) == duration

def test_get_owner(logs):
    """
    Given the logs code
    Return the name of logs owner
    """
    owner = logs.get_owner()
    
    assert owner
    assert owner == "Syqu22"


def test_get_zone(logs):
    """
    Given the logs code
    Return the zone id of logs
    """
    zone = logs.get_zone()

    assert zone
    assert zone == Zones.CASTLE_NATHRIA.value

def test_summary_events(logs):
    assert logs.get_events(Events.SUMMARY, logs.get_log_end())

def test_get_damage_events(logs):
    assert logs.get_events(Events.DAMAGE_DONE, logs.get_log_end())

def test_get_healing_events(logs):
    assert logs.get_events(Events.HEALING, logs.get_log_end())
