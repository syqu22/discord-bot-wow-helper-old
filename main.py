import os
from bot import bot
from dotenv import load_dotenv

# Read environment variables from .env
load_dotenv()


if __name__ == "__main__":
    # Start the bot
    bot.bot.run(os.getenv("DISCORD_TOKEN"))
