import requests
from events import Type

API_URL = "https://www.warcraftlogs.com:443/v1/report/"
CLIENT_KEY = "112af4ad330a251cbdc08faa580f3724"

class WarcraftlogsAPI():
    def __init__(self, code: str):
        self.code = code

    def get_fights(self):
        params = {
            "api_key": CLIENT_KEY,
            "translate": True
        }
        fights = requests.get(API_URL + "fights/" + self.code, params=params)
        
        if fights.status_code != 404:
            return fights.json()
        else:
            return None

    def get_events(self, view: Type, end: int, start: int = 0, source_id: int = None, cutoff: int = 3):
        params = {
            "view": view.value,
            "code": self.code,
            "cutoff": cutoff,
            "translate": True,
            "start": start,
            "end": end,
            "source_id": source_id,
            "api_key": CLIENT_KEY,
        }
        events = requests.get(API_URL + "tables/" + self.code, params=params)

        if events.status_code != 404:
            return events.json()
        else:
            return None
