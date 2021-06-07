from datetime import datetime
from math import floor

# H:M d-m-y
FIRST_WEEK = "8:00 9-12-2020"


class Affixes:
    # List of the affixes from Shadowlands Season 1
    affixes = [
        ["Fortified", "Bursting", "Volcanic", "Prideful"],  # Week 1 - First
        ["Tyrannical", "Bolstering", "Storming", "Prideful"],
        ["Fortified", "Spiteful", "Grievous", "Prideful"],
        ["Tyrannical", "Inspiring", "Necrotic", "Prideful"],
        ["Fortified", "Sanguine", "Quaking", "Prideful"],
        ["Tyrannical", "Raging", "Explosive", "Prideful"],
        ["Fortified", "Spiteful", "Volcanic", "Prideful"],
        ["Tyrannical", "Bolstering", "Necrotic", "Prideful"],
        ["Fortified", "Inspiring", "Storming", "Prideful"],
        ["Tyrannical", "Bursting", "Explosive", "Prideful"],
        ["Fortified", "Sanguine", "Grievous", "Prideful"],
        ["Tyrannical", "Raging", "Quaking", "Prideful"]]  # Week 12 - Last

    # week 1 = affixes[0]
    # week 26 = affixes[25]
    first_week = datetime.strptime(
        FIRST_WEEK, "%H:%M %d-%m-%Y").timestamp()

    def __init__(self):
        self.weeks_since_launch = self.calculate_current_week()

    @classmethod
    def calculate_current_week(cls) -> str:
        """
        Return current week of the season `int`
        """
        return floor(abs(cls.first_week - datetime.now().timestamp())/(60*60*24*7)) + 1

    def current_affixes(self) -> str:
        """
        Return affixes `str` from on current week
        """
        week = self.weeks_since_launch - 1
        while week > 11:
            week -= 12
        return ", ".join(self.affixes[week])

    def next_affixes(self) -> str:
        """
        Return affixes `str` from on next week
        """
        week = self.weeks_since_launch
        while week > 11:
            week -= 12
        return ", ".join(self.affixes[week])

    def previous_affixes(self) -> str:
        """
        Return affixes `str` from previous week
        """
        if self.weeks_since_launch - 1 < 1:
            return "No affixes"
        week = self.weeks_since_launch - 2
        while week > 11:
            week -= 12
        else:
            return ", ".join(self.affixes[week])

    def affixes_from_week(self, week: int) -> str:
        """
        Return affixes `str` from given week
        """
        if week < 1:
            return "No affixes"
        week -= 1
        while week > 11:
            week -= 12
        else:
            return ", ".join(self.affixes[week])
