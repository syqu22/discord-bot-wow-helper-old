from discord.embeds import Embed
from wow.blizzard import BlizzardAPI


class EmbedBlizzardMessage():
    async def create_token(self):
        try:
            blizzard = BlizzardAPI()
            embed_message = {
                "title": "WoW Tokens",
                "color": 4433254,
            }
            embed = Embed.from_dict(embed_message)
            tokens = await blizzard.get_wow_token_prices()
            for region, price in tokens.items():
                embed.add_field(
                    name=region.upper(), value="**{0:,}k** Gold".format(int(price)))

            return embed
        except:
            print(f"Token info not found")

            return Embed(title="WoW Token", description="Token info not found")

    async def create_character(self, name_realm: str, region: str):
        try:
            api = BlizzardAPI()
            name, realm = name_realm.split("-", 1)
            region = await normalize_region(region)

            character = await api.character_info(
                name, realm, region)

            armory_url = f"https://worldofwarcraft.com/en-gb/character/{region}/{realm}/{name}/"

            embed_message = {
                "title": f"({character.level}) {character.name}-{character.realm} {await set_guild(character.guild)}",
                "url": armory_url,
                "color": 4433254,
                "image": {
                    "url": await api.character_avatar(name, realm, region)
                }
            }
            embed = Embed.from_dict(embed_message)
            embed.add_field(
                name="Spec", value=f"{character.race} {character.spec} {character.char_class}")
            embed.add_field(
                name="Faction", value=f"{character.faction}"
            )
            embed.add_field(
                name="Item level", value=f"({character.ilvl}) {character.eq_ilvl}"
            )
            embed.add_field(
                name="Links", value=f"[Raider.IO](https://raider.io/characters/{region}/{realm}/{name}) | "
                f"[WarcraftLogs](https://www.warcraftlogs.com/character/{region}/{realm}/{name}) | "
                f"[WoWProgress](https://www.wowprogress.com/character/{region}/{realm}/{name})"
            )
            embed.add_field(
                name="Covenant", value=f"{character.covenant}",
            )
            embed.add_field(
                name="Achievements", value=f"[{character.ach_points}]({armory_url + 'achievements'})"
            )

            return embed
        except:
            print(
                f"Character {name}-{realm} with region {region} returned error")

            return Embed(title="Character", description="Wrong character name, realm or region. Remember to put "
                         "region after name-realm if the character is not on EU realm.")


async def normalize_region(region: str):
    if region:
        region = region.lower()

        if region == "na" or region == "us":
            return "us"
    # Default EU
    return "eu"


async def set_guild(guild: str):
    if guild:
        return f"<{guild}>"
    return " "
