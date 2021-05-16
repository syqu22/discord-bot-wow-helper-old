from datetime import datetime
from discord.embeds import Embed

DESCRIPTION = "Beep boob bop imam robot"
COLOR = 3066993
IMAGE_URL = "https://data1.cupsell.pl/upload/generator/10838/640x420/229559_print-trimmed-1.png?resize=max_sizes&key=55f9a22768eed085006592c1174c0235"

class EmbedLogsMesage():
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

    def create(self):
        embed_message = {
            "title": self.title,
            "description": DESCRIPTION,
            "url": self.url,
            "color": COLOR,
            "footer": {
                "text": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
            "image": {
                "url": IMAGE_URL
            },
            "fields": [{
                "name": "Pulls",
                "value": "etc."
            },{
                "name": "Parses",
                "value": "etc." 
            },{
                "name": "Deaths",
                "value": "etc." 
            }]
         }

        return Embed.from_dict(embed_message)
