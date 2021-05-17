import requests
from utils import Events, Metric, Player, Zones
from fight import Fight

API_URL = "https://www.warcraftlogs.com:443/v1/report/"
CLIENT_KEY = "112af4ad330a251cbdc08faa580f3724"
CURRENT_RAID = Zones.CASTLE_NATHRIA

class WarcraftlogsAPI():
    def __init__(self, code: str):
        self.code = code
        self.log_info = self.get_log_info()

    def get_log_info(self):
        params = {
            "api_key": CLIENT_KEY,
            "translate": True
        }
        fights = requests.get(API_URL + "fights/" + self.code, params=params)
        
        if fights.status_code == 200:
            return fights.json()
        else:
            return None

    def get_title(self):
        """
        Returns logs title
        """
        return self.log_info["title"]
    
    def get_characters(self):
        """
        Returns characters from logs
        """
        if self.get_zone() == Zones.TORGHAST.value:
            return "Torghast logs are not supported."
        elif self.get_zone() > Zones.CASTLE_NATHRIA.value:
            return "Characters cannot be accessed from PTR."
        else:
            return self.log_info["exportedCharacters"]

    def get_fight(self, fight_number):
        """
        Returns a Fight object

        :param id: returns the id of fight number in logs
        :param boss: returns the boss id
        :param start_time: returns a start time of the encounter in milliseconds (based on entire log)
        :param end_time: returns a end time of the encounter in milliseconds (based on entire log)
        :param duration: returns the duration of the fight in milliseconds
        :param name: returns name of the boss as a string
        :param zoneName: returns the zone name of the fight as a string
        :param difficulty: returns the fight difficulty (Mythic = 5)
        :param bossPercentage: returns boss health in % or an information that the boss died as a string
        :param rest: contain the rest of parameters that are less useful
        """
        fight = self.get_fights()[fight_number]
        return Fight(**fight)

    def get_fights(self):
        """
        Returns fights from logs as a list of dicts
        """  
        fights = self.log_info["fights"]
        fights[:] = [e for e in fights if e.get("boss")]
        return fights

    def get_fights_amount(self):
        """
        Returns the amount of fights as int
        """

        return len(self.get_fights())

    def get_duration(self):
        """
        Use only when you want end_time for events from entire logs
        Returns a duration of logs that is based on the first and last pull
        """
        return self.get_fights()[-1]["end_time"]

    def get_total_duration(self):
        """
        Use to determine time length of logs
        Return a duration of logs that comes from the difference of logs start time and end time
        """
        return abs(self.log_info["start"] - self.log_info["end"])

    def get_owner(self):
        """
        Returns the name of the logs owner as a string
        """
        return self.log_info["owner"]

    def get_zone(self):
        """
        Returns the id of the logs zone
        Check zones in utils/Zones
        """
        return self.log_info["zone"]


    # TODO EVENTS
    #def get_events(self, view: Events, source_id: int = None, cutoff: int = 3):
    #    params = {
    #        "code": self.code,
    #        "cutoff": cutoff,
    #        "translate": True,
    #        "start": 0,
    #        "end": self.get_duration(),
    #        "source_id": source_id,
    #        "api_key": CLIENT_KEY,
    #        "translate": True
    #    }
    #    print(API_URL + "tables/" + view.value + "/" + self.code)
    #    events = requests.get(API_URL + "tables/" + view.value + "/" + self.code, params=params)
    #
    #    if events.status_code == 200:
    #        return events.json()
    #    else:
    #        return None
    #
    #def get_rankings(self, encounter_id: int, metric: Metric, player_class: Player, player_spec: Player, page: int):
    #    params = {
    #        "metric": metric.value,
    #        "player_class": player_class.value,
    #        "player_spec": player_spec.value,
    #        "page": page,
    #        "includeCombatantInfo": False
    #    }
    #    rankings = requests.get(API_URL + "rankings/encounter/" + encounter_id, params=params)
    #
    #    if rankings.status_code == 200:
    #        return rankings.json()
    #    else:
    #        return None
