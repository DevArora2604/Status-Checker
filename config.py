from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "27353035"))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST").split())
CHANNEL_ID = int(getenv("CHANNEL_ID"))
MESSAGE_ID = int(getenv("MESSAGE_ID"))
GRP_ID = int(getenv("GRP_ID"))
SESSION = getenv("SESSION")
