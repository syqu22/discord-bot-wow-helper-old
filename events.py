from enum import Enum

class Type(Enum):
    SUMMARY = "summary"
    DAMAGE_DONE = "damage-done"   
    #DAMAGE_TAKEN = "damage-taken"
    HEALING = "healing"
    #CASTS = "casts"
    #SUMMONS = "summons"
    #BUFFS = "buffs"
    #DEBUFFS = "debuffs"
    #DEATHS = "deaths"
    #SURVIVABILITY = "survivability"
    #RESOURCES = "resources"
    #RESOUCES_GAINS = "resources-gains"

class Metric(Enum):
    DPS = "dps"
    HPS = "hps"
