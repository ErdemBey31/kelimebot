from time import sleep
from pyrogram import Client
import logging
from dotenv import load_dotenv, set_key, unset_key
from os import getenv

load_dotenv('config.env')

# THE LOGGING
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)


# Hesap
API_ID = 22414322
API_HASH = "d4ae0d06f838826fbcf1fa2dbe6b8f91"
TOKEN = "6585844649:AAGx2ubqydC1DFXyVkYZ4xRJGSAkuLs71yU"
USERNAME = "kelimeoyunurobot"
OWNER_ID = "6691596766"

if OWNER_ID and len(OWNER_ID) and OWNER_ID.isdigit():
    OWNER_ID = int(OWNER_ID)  # type: ignore
else:
    OWNER_ID = None  # type: ignore

# BOT CLIENTİ
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins=dict(root="kelime_bot/plugins/"),
    workers=16
)


# Oyun Verileri
oyun = {}  # type: ignore


# rating
rating = {}  # type: ignore
