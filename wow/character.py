# TODO Add __str__ and comments
class Character:
    def __init__(self, name: str, realm: str, level: int, faction: str, race: str, character_class: str, average_item_level: int, active_spec: str, guild: str, covenant_progress: str, achievement_points: int, **others: dict):
        self.name = name
        self.realm = realm["name"]
        self.level = level
        self.faction = faction["name"]
        self.race = race["name"]
        self.char_class = character_class["name"]
        self.ilvl = average_item_level
        self.spec = active_spec["name"]
        self.guild = self.set_guild_name(guild["name"], guild["realm"]["name"])
        self.covenant = self.set_covenant(
            covenant_progress["chosen_covenant"]["name"], covenant_progress["renown_level"])
        self.ach_points = achievement_points
        self.others = others

    def set_guild_name(self, name: str, realm: str):
        return f"{name}-{realm}"

    def set_covenant(self, covenant: str, renown: int):
        return f"{covenant} ({renown})"
