class Character:
    """
    Parameters
    -----------
        name: `str`
            Name of the character
        realm: `str`
            Realm of the character
        level: `int`
            Level of the character
        faction: `str`
            Faction of the character
        race: `str`
            Race of the character
        spec: `str`
            Spec of the character
        char_class: `str`
            Class of the character
        ilvl: `int`
            Item level of the character
        eq_ilvl: `int`
            Equipped Item level of the character
        guild: `str`
            Guild name of the character
        covenant: `str`
            Covenant of the character and renown level
        ach_points: `int`
            Amount of achievements points the character has
        others: `dict`
            Other not used parameters
        """

    def __init__(self, name: str, realm: str, level: int, faction: str, race: str, active_spec: str, character_class: str, average_item_level: int, equipped_item_level: int, guild: str, covenant_progress: str, achievement_points: int, **others: dict):
        self.name = name
        self.realm = realm["name"]
        self.level = level
        self.faction = faction["name"]
        self.race = race["name"]
        self.spec = active_spec["name"]
        self.char_class = character_class["name"]
        self.ilvl = average_item_level
        self.eq_ilvl = equipped_item_level
        self.guild = guild["name"]
        self.covenant = self.set_covenant(
            covenant_progress["chosen_covenant"]["name"], covenant_progress["renown_level"])
        self.ach_points = achievement_points
        self.others = others

    def set_covenant(self, covenant: str, renown: int):
        return f"{covenant} ({renown})"

    def __str__(self):
        return f"{self.name}-{self.realm} ({self.level}) [{self.faction}] {self.race} {self.spec} {self.char_class} {self.ilvl} {self.guild} {self.covenant} {self.ach_points}"
