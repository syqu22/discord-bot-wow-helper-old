import os
import aiohttp
import logging
from wow.fight import Fight
from asyncinit import asyncinit

_logger = logging.getLogger("discord")

API_URL = "https://www.warcraftlogs.com:443/v1/report/"


@asyncinit
class WarcraftlogsAPI():
    async def __init__(self, code: str):
        self.code = code
        self.log_info = await self.get_log_info()

    async def get_log_info(self):
        try:
            async with aiohttp.ClientSession() as session:
                params = {
                    "api_key": os.getenv("WARCRAFTLOGS_CLIENT"),
                    "translate": "True"
                }
                async with session.get(API_URL + "fights/" +
                                       self.code, params=params) as resp:
                    return await resp.json()
        except:
            _logger.error(
                f"There was an error while getting logs info with {self.code} code")
            return None

    async def get_title(self):
        """
        Return the logs title `str`
        """
        return (self.log_info)["title"]

    async def get_fight(self, fight_number):
        """
        Return the `Fight` object from `list` of fights
        with the given fight_number
        """
        fight = (await self.get_fights())[fight_number]
        return Fight(**fight)

    async def get_fights(self):
        """
        Return `list` of `dict` fights from logs
        (excluding trash and reset pulls if it is raid)
        """
        fights = (self.log_info)["fights"]
        fights[:] = [e for e in fights if e.get("boss")]
        return fights

    async def get_fights_amount(self):
        """
        Return the :`int` number of fights
        """
        return len(await self.get_fights())

    async def get_total_duration(self):
        """
        Use to calculate duration of logs

        Return the `int` duration of logs that comes from the
        difference of first and last event
        """
        return abs((self.log_info)["start"] - (self.log_info)["end"])

    async def get_zone(self):
        """
        Return the name of the logs zone as an `str`

        MYTHIC_PLUS = 25
        CASTLE_NATHRIA = 26
        TORGHAST = 27
        SANCTUM_OF_DOMINATION = 28
        NEXT_RAID = 29...
        """
        zone = (self.log_info)["zone"]
        if zone == 25:
            return "Mythic+"
        elif zone == 26:
            return "Castle Nathria"
        elif zone == 27:
            return "Torghast"
        elif zone == 28:
            return "Sanctum of Domination"
        elif zone == 29:
            return "Future raid..."
        else:
            return None
