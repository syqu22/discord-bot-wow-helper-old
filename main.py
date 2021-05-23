from bot import bot
from requests_cache import install_cache

if __name__ == "__main__":
    install_cache("cache", expire_after=300)
    bot.bot.run(bot.get_token())
