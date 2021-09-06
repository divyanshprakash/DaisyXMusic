import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = 'AQA1Gk7wEdjaMZVnQmbwyI9XNZOkFUtD-rxWYbWdDDETTHRSvA1Bwkji8MAvhsN7NTIHhWY-Yce-jcM2YVuq9YT8GEqiDwSUUWU7gvgavXiKdcmYXc-rB_JbprPMRyanhjL65vG8GNW96yQSRTB9eLOUjGcaqMJy2pfeOwpIkwkMjIMbyq_YFCj3NAiR9u8kalvKwGHIKGfNAdiB8cFIoGt_-eH2A8fZle2N7Fic-YtPmp0s6Wl1pQytt3jGvGt3TzU8QasKVL6H9PaIcnC9rej-RuPW9UHIEy70UCAPEx4RnC3x3EhgIU320v1eSEGKAm2Lu-r5opMPWfeCyEwSgHvcckfQFwA'
BOT_TOKEN = "1974969627:AAGIOy8TKG_P3TeKrrcvRfsAB56nyQPA_ik"
BOT_NAME = getenv("royal Music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "the_royal_music")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID =  7706870
API_HASH = "6982374bef85e9953a1ee53a02e92991"
BOT_USERNAME = getenv("mr_royal_music_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ADDDMEEKEKIEEJHE")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AnonymousArmy_1")
PROJECT_NAME = getenv("PROJECT_NAME", "Royal Music")
SUPPORT = getenv("SUPPORT", "https://telegra.ph/SUPPORT-08-01-2")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70000"))
ARQ_API_KEY = "BZWLAO-CLDVIK-DBEOWZ-VYLIOI-ARQ"
PMPERMIT = getenv("on")
LOG_GRP = "-1001591741014"
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = "691224603"
