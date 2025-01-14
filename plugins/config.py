import os

import logging

logging.basicConfig(

    format='%(name)s - %(levelname)s - %(message)s',

    handlers=[logging.FileHandler('log.txt'),

              logging.StreamHandler()],

    level=logging.INFO

)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6244236878:AAERMGwn0uZoFQUqlgnUJtMK1mPsRIvgRIQ")

    API_ID = int(os.environ.get("API_ID", "28082960"))

    API_HASH = os.environ.get("API_HASH", "eff07a6fd1fd581be959970ee7c06962")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6009081395").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001807115974")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @AnydownloadDJ_bot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Bhajanpreet:5843956Abc@cluster0.dgvr0rx.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "AnydownloadDJ_bot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001807115974))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "6009081395"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001807115974")

    

    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AnydownloadDJ_bot")
























   







