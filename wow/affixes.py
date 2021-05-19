from datetime import datetime

# H:M d-m-y
FIRST_WEEK = "8:00 8-12-2020"
FIRST_EU_AFFIX = 4


class Affixes:

    affixes = [[
        10, 122, 124, 121],  # Week 1 - First
        [9, 11, 13, 121],
        [10, 8, 12, 121],
        [9, 6, 14, 121],
        [10, 11, 3, 121],  # First affix set of Season 1 [4]
        [9, 7, 124, 121],
        [10, 123, 12, 121],
        [9, 122, 4, 121],
        [10, 8, 14, 121],
        [9, 6, 13, 121],
        [10, 123, 3, 121],
        [9, 7, 4, 121]]  # Week 12 - Last

    first_week = datetime.strptime(
        FIRST_WEEK, "%H:%M %d-%m-%Y").timestamp()

    def __init__(self):
        self.weeks_since_launch = round(
            self.calculateCurrentWeek()) + FIRST_EU_AFFIX
        self.current = self.getCurrentAffixes()
        self.next = self.getNextWeekAffixes()
        self.previous = self.getPreviousWeekAfixes()

    @classmethod
    def calculateCurrentWeek(cls):
        return abs(cls.first_week - datetime.now().timestamp())/(60*60*24*7)

    def getCurrentAffixes(self):
        while self.weeks_since_launch > 12:
            self.weeks_since_launch -= 12
        return self.affixes[self.weeks_since_launch]

    def getNextWeekAffixes(self):
        while self.weeks_since_launch + 1 > 12:
            self.weeks_since_launch -= 12
        return self.affixes[self.weeks_since_launch + 1]

    def getPreviousWeekAfixes(self):
        while self.weeks_since_launch - 1 > 12:
            self.weeks_since_launch -= 12
        return self.affixes[self.weeks_since_launch - 1]
