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
            Other parameters like:
                - covenant_progress
        """

    def __init__(self, name: str, realm: str, level: int, faction: str, race: str, active_spec: str, character_class: str, average_item_level: int, equipped_item_level: int, guild: str, achievement_points: int, **others: dict):
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
        self.others = others
        self.covenant = self.set_covenant()
        self.ach_points = achievement_points

    def set_covenant(self):
        covenant = self.others.get("covenant_progress")
        if covenant:
            name = covenant["chosen_covenant"]["name"]
            level = covenant["renown_level"]
            return f"{name} ({level})"

        return None

    def __str__(self):
        return f"{self.name}-{self.realm} ({self.level}) [{self.faction}] {self.race} {self.spec} {self.char_class} {self.ilvl} {self.guild} {self.covenant} {self.ach_points}"
