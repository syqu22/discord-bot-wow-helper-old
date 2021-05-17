class Fight(object):
    """
    Parameters
    -----------
        id: `int`
            ID of the fight number
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
        rest: `dict`
            Rest of the less useful parameters
        """
    def __init__(self, id: int, boss: int, start_time: int, end_time: int, name: str, zoneName: str, difficulty: int, bossPercentage: int, **rest: dict):
        self.id = id
        self.boss = boss
        self.start_time = start_time
        self.end_time = end_time
        self.duration = self.get_duration()
        self.name = name
        self.zoneName = zoneName
        self.difficulty = difficulty
        self.rest = rest
        self.bossPercentage = self.set_bossPercentage(bossPercentage)

    def set_bossPercentage(self, bossPercentage: int):
        if self.rest["kill"] == True:
            return "Dead!"
        else:
            return str(bossPercentage / 100) + "%"

    def get_duration(self):
        return abs(self.start_time - self.end_time)
