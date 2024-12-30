# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# AUTH_CHANNEL Configuration
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', 'Prime_Movies4U Prime_Botz +DnOsTWqbm8hjYmQ1').split()]

# Function to Check and Apply Join Mode
def get_channel_mode(channel_id):
    if str(channel_id) == '-1002296355008':  # Replace with the specific channel ID for 'Request to Join'
        return "request_to_join"
    else:
        return "direct_join"

# Function to Generate Join Link
def generate_join_link(channel_id):
    join_mode = get_channel_mode(channel_id)
    if join_mode == "request_to_join":
        return f"https://t.me/{channel_id}?join_request=1"
    else:
        return f"https://t.me/{channel_id}"

# Example Usage (Optional)
if __name__ == "__main__":
    for channel in AUTH_CHANNEL:
        join_mode = get_channel_mode(channel)
        join_link = generate_join_link(channel)
        print(f"Channel {channel}: Mode - {join_mode}, Link - {join_link}")
# Bot Information
API_ID = int(environ.get("API_ID", "25425840"))
API_HASH = environ.get("API_HASH", "e6ea2eca4aa38e965511f323e5ffa578")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

PICS = (environ.get('PICS', 'https://envs.sh/1fu.jpg')).split() # Bot Start Picture
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7057105056').split()]
BOT_USERNAME = environ.get("BOT_USERNAME", "Prime_Movies_Store_Robot") # without @
PORT = environ.get("PORT", "8080")

# Clone Info :-
CLONE_MODE = bool(environ.get('CLONE_MODE', True)) # Set True or False

# If Clone Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
CLONE_DB_URI = environ.get("CLONE_DB_URI", "mongodb+srv://vogaje4812:zSXRd584CxoK8wEQ@cluster0.tnwxw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CDB_NAME = environ.get("CDB_NAME", "PrimeBotz")

# Database Information
DB_URI = environ.get("DB_URI", "mongodb+srv://shnayembd1:XAuVBX2Se3iFSnwa@cluster0.rha6xvq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "PrimeBotx")

# Auto Delete Information
AUTO_DELETE_MODE = bool(environ.get('AUTO_DELETE_MODE', True)) # Set True or False

# If Auto Delete Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
AUTO_DELETE = int(environ.get("AUTO_DELETE", "20")) # Time in Minutes
AUTO_DELETE_TIME = int(environ.get("AUTO_DELETE_TIME", "1800")) # Time in Seconds

# Channel Information
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002184630716"))

# File Caption Information
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)

# Enable - True or Disable - False
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Verify Info :-
VERIFY_MODE = bool(environ.get('VERIFY_MODE', False)) # Set True or False

# If Verify Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
SHORTLINK_URL = environ.get("SHORTLINK_URL", "api.shareus.io") # shortlink domain without https://
SHORTLINK_API = environ.get("SHORTLINK_API", "hRPS5vvZc0OGOEUQJMJzPiojoVK2") # shortlink api
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/How_To_Open_Linkl") # how to open link 

# Website Info:
WEBSITE_URL_MODE = bool(environ.get('WEBSITE_URL_MODE', False)) # Set True or False

# If Website Url Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
WEBSITE_URL = environ.get("WEBSITE_URL", "https://primehub1.blogspot.com/2024/10/prime.html") # For More Information Check Video On Yt - @Tech_VJ

# File Stream Config
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Set True or False

# If Stream Mode Is True Then Fill All Required Variable, If False Then Don't Fill.
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("URL", "")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
    
