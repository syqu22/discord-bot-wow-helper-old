from enum import Enum

class Events(Enum):
    SUMMARY = "summary"
    DAMAGE_DONE = "damage-done"   
    #DAMAGE_TAKEN = "damage-taken"
    HEALING = "healing"
    #CASTS = "casts"
    #SUMMONS = "summons"
    #BUFFS = "buffs"
    #DEBUFFS = "debuffs"
    DEATHS = "deaths"
    #SURVIVABILITY = "survivability"
    #RESOURCES = "resources"
    #RESOUCES_GAINS = "resources-gains"

class Metric(Enum):
    DPS = "dps"
    HPS = "hps"

class Zones(Enum):
    MYTHIC_PLUS = 25
    CASTLE_NATHRIA = 26
    TORGHAST = 27
    SANCTUM_OF_DOMINATION = 28

class Player(Enum):
    DK = 1
    DK_BLOOD = 1
    DK_FROST = 2
    DK_UNHOLY = 3

    DRUID = 2
    DRUID_BALANCE = 1
    DRUID_FERAL = 2
    DRUID_GUARDIAN = 3
    DRUID_RESTORATION = 4

    HUNTER = 3
    HUNTER_BM = 1
    HUNTER_MM = 2
    HUNTER_SURVIVAL = 3

    MAGE = 4
    MAGE_ARCANE = 1
    MAGE_FIRE = 2
    MAGE_FROST = 3

    MONK = 5
    MONK_BM = 1
    MONK_MW = 2
    MONK_WW = 3

    PALADIN = 6
    PALADIN_HOLY = 1
    PALADIN_PROT = 2
    PALADIN_RET = 3

    PRIEST = 7
    PRIEST_DISC = 1
    PRIEST_HOLY = 2
    PRIEST_SHADOW = 3

    ROGUE = 8
    ROGUE_ASSA = 1
    ROGUE_SUB = 3
    ROGUE_OUTLAW = 4

    SHAMAN = 9
    SHAMAN_ELE = 1
    SHAMAN_ENH = 2
    SHAMAN_RESTO = 3

    WARLOCK = 10
    WARLOCK_AFFLI = 1
    WARLOCK_DEMO = 2
    WARLOCK_DESTRUCTION = 3

    WARRIOR = 11
    WARRIOR_ARMS = 1
    WARRIOR_FURY = 2
    WARRIOR_PROT = 3

    DH = 12
    DH_HAVOC = 1
    DH_VENG = 2
