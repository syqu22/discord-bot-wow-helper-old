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
    affixes.weeks_since_launch = 9
    return affixes


def test_weeks_since_launch(affixes):
    """
    Given the affixes fixture
    Return valid number of weeks since launch
    """
    assert isinstance(affixes.weeks_since_launch, int)
    assert affixes.weeks_since_launch == 9


def test_current_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from current week
    """
    current_affixes = affixes.current_affixes()
    correct_affixes = ", ".join(
        ["Tyrannical", "Inspiring", "Quaking", "Tormented"])

    assert isinstance(current_affixes, str)
    assert current_affixes == correct_affixes
    assert "Bolstering" not in current_affixes


def test_next_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from incoming week
    """
    next_affixes = affixes.next_affixes()
    correct_affixes = ", ".join(
        ["Fortified", "Sanguine", "Necrotic", "Tormented"])

    assert isinstance(next_affixes, str)
    assert next_affixes == correct_affixes
    assert "Bolstering" not in next_affixes


def test_previous_affixes(affixes):
    """
    Given the affixes fixture
    Return correct affixes from previous week
    """
    previous_affixes = affixes.previous_affixes()
    correct_affixes = ", ".join(
        ["Fortified", "Spiteful", "Grievous", "Tormented"])

    assert isinstance(previous_affixes, str)
    assert previous_affixes == correct_affixes
    assert "Explosive" not in previous_affixes


def test_affixes_from_week():
    """
    Return correct affixes from given week
    """
    week = 1
    affixes_from_week = Affixes().affixes_from_week(week)
    correct_affixes = ", ".join(
        ["Tyrannical", "Raging", "Volcanic", "Tormented"])

    assert isinstance(affixes_from_week, str)
    assert affixes_from_week == correct_affixes
    assert "Explosive" not in affixes_from_week
