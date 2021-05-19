from datetime import datetime

# H:M d-m-y
FIRST_WEEK = "8:00 8-12-2020"
FIRST_EU_AFFIX = 4


class Affixes:
    affixes = [[
        "Fortified", "Inspiring", "Storming", "Prideful"],  # Week 1 - First
        ["Tyrannical", "Bursting", "Explosive", "Prideful"],
        ["Fortified", "Sanguine", "Grievous", "Prideful"],
        ["Tyrannical", "Raging", "Quaking", "Prideful"],
        ["Fortified", "Bursting", "Volcanic", "Prideful"],
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
            self.calculateCurrentWeek()) + FIRST_EU_AFFIX

    @classmethod
    def calculateCurrentWeek(cls):
        return abs(cls.first_week - datetime.now().timestamp())/(60*60*24*7)

    def currentAffixes(self):
        while self.weeks_since_launch > 12:
            self.weeks_since_launch -= 12
        return ", ".join(self.affixes[self.weeks_since_launch])

    def nextWeekAffixes(self):
        while self.weeks_since_launch + 1 > 12:
            self.weeks_since_launch -= 12
        return ", ".join(self.affixes[self.weeks_since_launch + 1])

    def previousWeekAfixes(self):
        while self.weeks_since_launch - 1 > 12:
            self.weeks_since_launch -= 12
        return ", ".join(self.affixes[self.weeks_since_launch - 1])

    def affixesFromWeek(self, week: int):
        week += FIRST_EU_AFFIX
        while week > 12:
            week -= 12
        return ", ".join(self.affixes[week])
