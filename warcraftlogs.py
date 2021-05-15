import requests
from enums import Events, Metric, Player

API_URL = "https://www.warcraftlogs.com:443/v1/report/"
CLIENT_KEY = "112af4ad330a251cbdc08faa580f3724"

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
        
        if fights.status_code != 404:
            return fights.json()
        else:
            return None

    def get_title(self):
        return self.log_info["title"]
    
    def get_characters(self):
        return self.log_info["exportedCharacters"]

    def get_fights(self):
        return self.log_info["fights"]

    def get_log_duration(self):
        return abs(self.log_info["start"] - self.log_info["end"])

    def get_zone(self):
        return self.log_info["owner"]

    def get_game_version(self):
        return self.log_info["gameVersion"]

    def get_events(self, view: Events, end: int, start: int = 0, source_id: int = None, cutoff: int = 3):
        params = {
            "code": self.code,
            "cutoff": cutoff,
            "translate": True,
            "start": start,
            "end": end,
            "source_id": source_id,
            "api_key": CLIENT_KEY,
            "translate": True
        }
        print(API_URL + "tables/" + view.value + "/" + self.code)
        events = requests.get(API_URL + "tables/" + view.value + "/" + self.code, params=params)

        if events.status_code != 404:
            return events.json()
        else:
            return None

    def get_rankings(self, encounter_id: int, metric: Metric, player_class: Player, player_spec: Player, page: int):
        params = {
            "metric": metric.value,
            "player_class": player_class.value,
            "player_spec": player_spec.value,
            "page": page,
            "includeCombatantInfo": False
        }
        rankings = requests.get(API_URL + "rankings/encounter/" + encounter_id, params=params)

        if rankings.status_code != 404:
            return rankings.json()
        else:
            return None
