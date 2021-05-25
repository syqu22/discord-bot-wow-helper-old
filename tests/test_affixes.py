"""
This file contains unit tests for the Affixes class
"""
import pytest
from wow.affixes import Affixes


@pytest.fixture(scope="module")
def affixes():
    """
    Affixes fixture that changes variable to single week
    """
    affixes = Affixes()
    affixes.weeks_since_launch = 27
    return affixes


def test_weeks_since_launch(affixes):
    """
    Given the affixes fixture
    Return valid number of weeks since launch
    """
    assert isinstance(affixes.weeks_since_launch, int)
    assert affixes.weeks_since_launch == 27


def test_current_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from current week
    """
    current_affixes = affixes.current_affixes()

    assert isinstance(current_affixes, str)
    assert "Fortified" in current_affixes
    assert "Spiteful" in current_affixes
    assert "Grievous" in current_affixes
    assert "Prideful" in current_affixes
    assert "Quaking" not in current_affixes


def test_next_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from incoming week
    """
    next_affixes = affixes.next_affixes()

    assert isinstance(next_affixes, str)
    assert "Tyrannical" in next_affixes
    assert "Inspiring" in next_affixes
    assert "Necrotic" in next_affixes
    assert "Prideful" in next_affixes
    assert "Bolstering" not in next_affixes


def test_previous_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from previous week
    """
    previous_affixes = affixes.previous_affixes()

    assert isinstance(previous_affixes, str)
    assert "Tyrannical" in previous_affixes
    assert "Bolstering" in previous_affixes
    assert "Storming" in previous_affixes
    assert "Prideful" in previous_affixes
    assert "Volcanic" not in previous_affixes


def test_affixes_from_week():
    """
    Return correct affixes from given week
    """
    week = 1
    affixes_from_week = Affixes().affixes_from_week(week)

    assert isinstance(affixes_from_week, str)
    assert "Fortified" in affixes_from_week
    assert "Bursting" in affixes_from_week
    assert "Volcanic" in affixes_from_week
    assert "Prideful" in affixes_from_week
    assert "Bolstering" not in affixes_from_week
