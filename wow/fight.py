class Fight(object):
    """
    Parameters
    -----------
        id: `int`
            ID of the fight number (including trash packs)
        boss: `int`
            ID of the boss
        start_time: `int` 
            Start time of the figth in milliseconds
        end_time: `int`
            End time of the fight in milliseconds
        duration: `int`
            Duration of the fight in milliseconds
        name: `str`
            Name of the boss
        zoneName: `str`
            Name of the zone
        difficulty: `int`
            Fight difficulty (Mythic = 5)
        bossPercentage: `str`
            Boss health in % or an information that the boss died
        others: `dict`
            Other parameters like: 
                - bossPercentage (boss health `int`)
                - kill (is boss dead or not `bool`)
        """

    def __init__(self, id: int, boss: int, start_time: int, end_time: int, name: str, zoneName: str, **others: dict):
        self.id = id
        self.boss = boss
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self.set_duration()
        self.name = name
        self.zoneName = zoneName
        self.others = others
        # Check if fight contains every information (m+ logs do not have these)
        if "difficulty" in self.others:
            self.difficulty = self.set_difficulty(others["difficulty"])
            self.bossPercentage = self.set_bossPercentage(
                others["bossPercentage"])

    def set_bossPercentage(self, bossPercentage: int):
        if self.others["kill"] == True:
            return "Dead!"
        else:
            return str(bossPercentage / 100) + "%"

    def set_difficulty(self, difficulty: int):
        """
        1 = LFR
        3 = Normal
        4 = Heroic
        5 = Mythic
        """
        if difficulty == 5:
            return "Mythic"
        if difficulty == 4:
            return "Heroic"
        if difficulty == 3:
            return "Normal"
        if difficulty == 1:
            return "LFR"

    def set_duration(self):
        return abs(self.start_time - self.end_time)