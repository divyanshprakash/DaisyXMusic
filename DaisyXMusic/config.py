import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = 'AQClM8fx7RBkbx3W1LjETyXWIOqNorR24S52EPnz3VdH3c6nWHbMNEMgB5fUqSax_bFNa4_nFBfR0MWikt6BE73QTc7TTP4mZGSKFqBtieJhj2NKd_112ZIL0bvJGAQSMqP5-efLnLUENj8BHRBGqkAzTnY1WFqozKQnkJWvtRFFOW7XqVljDd6phJpXYzoWb_fKIukx1sCEXIouuKbHtQwsGW_ycAC_0Ght1b4lnZ85LgnF_hlOBc29wmcUmflhsfR-EgvRk5MK4agKHcYB0o01Bvx1A1oZ6S5pJ9eMUiI7abuiQseK0BlZsDwcGr7SMNCpAwX-1j4aAjKIGgiLayOyckfQFwA'
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
SOURCE_CODE = getenv("SUPPORT", "https://telegra.ph/SUPPORT-08-01-2")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "70000"))
ARQ_API_KEY = "BZWLAO-CLDVIK-DBEOWZ-VYLIOI-ARQ"
PMPERMIT = getenv("on")
LOG_GRP = "-1001591741014"
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = "691224603"
