from datetime import datetime

# H:M d-m-y
FIRST_WEEK = "8:00 9-12-2020"
# First week of EU
FIRST_AFFIX = 3


class Affixes:
    # List of the affixes from Shadowlands Season 1
    affixes = [[
        "Fortified", "Inspiring", "Storming", "Prideful"],  # Week 1 - First
        ["Tyrannical", "Bursting", "Explosive", "Prideful"],
        ["Fortified", "Sanguine", "Grievous", "Prideful"],
        ["Tyrannical", "Raging", "Quaking", "Prideful"],
        ["Fortified", "Bursting", "Volcanic", "Prideful"],  # First week of EU
        ["Tyrannical", "Bolstering", "Storming", "Prideful"],
        ["Fortified", "Spiteful", "Grievous", "Prideful"],
        ["Tyrannical", "Inspiring", "Necrotic", "Prideful"],
        ["Fortified", "Sanguine", "Quaking", "Prideful"],
        ["Tyrannical", "Raging", "Explosive", "Prideful"],
        ["Fortified", "Spiteful", "Volcanic", "Prideful"],
        ["Tyrannical", "Bolstering", "Necrotic", "Prideful"]]  # Week 12 - Last

    first_week = datetime.strptime(
        FIRST_WEEK, "%H:%M %d-%m-%Y").timestamp()

    def __init__(self):
        self.weeks_since_launch = round(
            self.calculate_current_week())

    @classmethod
    def calculate_current_week(cls):
        """
        Return current week of the season `int`
        """
        return abs(cls.first_week - datetime.now().timestamp())/(60*60*24*7)

    def current_affixes(self):
        """
        Return affixes `str` from on current week
        """
        week = self.weeks_since_launch + FIRST_AFFIX
        while week > 12:
            week -= 12
        return ", ".join(self.affixes[week])

    def next_affixes(self):
        """
        Return affixes `str` from on next week
        """
        week = self.weeks_since_launch + FIRST_AFFIX
        while week + 1 > 12:
            week -= 12
        return ", ".join(self.affixes[week + 1])

    def previous_affixes(self):
        """
        Return affixes `str` from previous week
        """
        week = self.weeks_since_launch + FIRST_AFFIX
        while week - 1 > 12:
            week -= 12
        if week - 1 < 1:
            return "No affixes"
        else:
            return ", ".join(self.affixes[week - 1])

    def affixes_from_week(self, week: int):
        """
        Return affixes `str` from given week
        """
        week += FIRST_AFFIX
        while week > 12:
            week -= 12
        if week < 1:
            return "No affixes"
        else:
            return ", ".join(self.affixes[week])
