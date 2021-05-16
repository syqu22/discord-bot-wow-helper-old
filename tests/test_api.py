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

def test_get_fight(logs):
    """
    Given the logs code
    Return a namedtuple fight object
    """
    fight = logs.get_fight(2)

    assert fight
    assert fight.name == "Stone Legion Generals"
    assert fight.start_time == 759237  
    assert fight.end_time == 766400 
    assert fight.boss == 0

def test_get_fights(logs):
    """
    Given the logs code
    Return a list of dicts of fights
    """
    fights = logs.get_fights()

    assert type(fights) == list
    assert [x["boss"] and x["id"] and x["name"] and x["bossPercentage"] and x["start_time"] and x["end_time"] and x["difficulty"] for x in fights]
    assert next(x for x in fights if x["name"] == "Sire Denathrius" and "Sludgefist" and "Stone Legion Generals")

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

def test_get_logs_duration(logs):
    """
    Given the logs code
    Return the zone id of logs
    """
    duration = logs.get_logs_duration()

    assert duration
    assert duration == 10700162

def test_get_logs_total_duration(logs):
    """
    Given the logs code
    Return a duration of logs that comes from the difference of logs start time and end time
    """
    duration = logs.get_logs_total_duration()

    assert duration
    assert type(duration) == int
    assert duration == 10905831

#def test_summary_events(logs):
#    events = logs.get_events(Events.SUMMARY)
#
#    assert events
#    assert events == 1

#def test_get_damage_events(logs):
#    assert logs.get_events(Events.DAMAGE_DONE)

#def test_get_healing_events(logs):
#    assert logs.get_events(Events.HEALING)

#def test_get_deaths_events(logs):
#    assert logs.get_events(Events.HEALING)
