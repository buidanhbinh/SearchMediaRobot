import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_Search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Telegram Movie Search Bot**

Here You Can Search Files In Inline Mode. Just Press SEARCH Button & Type A Movie Name!
"""

HELP_MSG = """
🙋 Hey Bruh, \nYou Can Use Me For Searching Any Media Files Like New Movies, Web Series, Cartoons From Inline Mode Across Telegram. Just Type My Username Anywhere In Telegram Message Box & Type Movies/Web Series/Cartoons Name To Search.

**Example:** `@SearchMediaRobot Master 2021`
 """

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = '🙋 Hey Bruh, Checkout **{username}** For Searching Media Files Like Movies, Web Series, Cartoons Etc. You Can Also Use This Bot In Inline Mode On Any Chat Of Telegram.'
INVITE_MSG = environ.get('INVITE_MSG', 'Please Join @AsmSafone To Use Me!')
