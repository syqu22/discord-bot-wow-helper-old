import requests
from wow.fight import Fight

API_URL = "https://www.warcraftlogs.com:443/v1/report/"
CLIENT_KEY = "112af4ad330a251cbdc08faa580f3724"


class WarcraftlogsAPI():
    def __init__(self, code: str):
        self.code = code
        self.log_info = self.get_log_info()

    def get_log_info(self):
        try:
            params = {
                "api_key": CLIENT_KEY,
                "translate": True
            }
            fights = requests.get(API_URL + "fights/" +
                                  self.code, params=params)
            return fights.json()
        except:
            return None

    def get_title(self):
        """
        Returns the logs title `str`
        """
        return self.log_info["title"]

    def get_characters(self):
        """
        Returns a `dict` of characters from logs
        """
        return self.log_info["exportedCharacters"]

    def get_fight(self, fight_number):
        """
        Returns the `Fight` object from `list` of fights
        with the given fight_number
        """
        fight = self.get_fights()[fight_number]
        return Fight(**fight)

    def get_fights(self):
        """
        Returns `list` of `dict` fights from logs
        (excluding trash and reset pulls if it is raid)
        """
        fights = self.log_info["fights"]
        fights[:] = [e for e in fights if e.get("boss")]
        return fights

    def get_fights_amount(self):
        """
        Returns the :`int` number of fights
        """
        return len(self.get_fights())

    def get_duration(self):
        """
        Use for events when you need to check entire logs timeline.

        Returns the `int` duration of logs that is based on the first and last pull
        """
        return self.get_fights()[-1]["end_time"]

    def get_total_duration(self):
        """
        Use to calculate duration of logs

        Returns the `int` duration of logs that comes from the
        difference of first and last event
        """
        return abs(self.log_info["start"] - self.log_info["end"])

    def get_owner(self):
        """
        Returns the `str` name of the logs owner
        """
        return self.log_info["owner"]

    def get_zone(self):
        """
        Returns the name of the logs zone as an `str`

        MYTHIC_PLUS = 25
        CASTLE_NATHRIA = 26
        TORGHAST = 27
        SANCTUM_OF_DOMINATION = 28
        NEXT_RAID = 29...
        """
        zone = self.log_info["zone"]
        if zone == 26:
            return "Castle Nathria"
        elif zone == 28:
            return "Sanctum of Domination"
        elif zone == 29:
            return "Future raid..."
        else:
            return None
