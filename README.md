

# flask-pastebin

<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/avatar.png" height=50% width=60%>

Discord bot based on [discord.py](https://discordpy.readthedocs.io/en/stable/) written in Python.

Technology I have used:
- `discord.py` for easier and better usage of Discord API
- `python-blizzardapi` for fetching Blizzard data
- `aiohttp` for asynchronous requests
- `pytest` for testing

## Commands

- ?ping - Pong?
- ?log - Return a list of fights with link to each fight, boss health percentage and fight duration
- ?character - [region] - Get simple data about a given character and with links to some popular 
- ?affixes [week] - Check for current/future/previous or any other given week affixes
- ?token - Check the current price of WoW token

## [Invite Link](https://discord.com/api/oauth2/authorize?client_id=842687783523844149&permissions=67584&scope=bot)
## Screenshots
<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/affixes_1_command.png" height=50% width=60%>
<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/affixes_2_command.png" height=50% width=60%>
<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/character_command.png" height=50% width=60%>
<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/logs_command.png" height=50% width=60%>
<img src="https://github.com/syqu22/discord-bot-wow-helper/blob/main/img/token_command.png" height=50% width=60%>

## Installation 

If you want to use this bot locally for yourself

1. First clone the repository:
    ```sh
    $ git clone https://github.com/syqu22/discord-bot-wow-helper.git
    ```

2. Then install all required libraries through:
    ```sh
    $ pip install -r requirements.txt
    ```

Remember to put in environment keys, first change the file name of `.env.sample` to `.env` then fill it with required keys. `DISCORD_TOKEN` is the most important one, without it your bot won't start.

There's also a possibility to build container using Docker, simply type:

```sh
$ docker-compose -f "docker-compose.yml" up -d --build
```
