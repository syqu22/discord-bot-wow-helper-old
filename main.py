import os
from bot import bot
from dotenv import load_dotenv
from requests_cache import install_cache

# Read environment variables from .env
load_dotenv()


if __name__ == "__main__":
    # Add cache to API requests
    install_cache("cache", expire_after=300)
    bot.bot.run(os.getenv("DISCORD_TOKEN"))
