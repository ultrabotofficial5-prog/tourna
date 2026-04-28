import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TORTOISE = {
    "connections": {
         # PostgreSQL connection URL: postgres://username@localhost:5432/database_name
         "default": os.getenv("DATABASE_URL", "postgres://sachin@localhost:5432/quotient_db"),
    },
    "apps": {
        "models": {
            "models": [
                "models.misc",
                "models", 
                "aerich.models"
            ],
            "default_connection": "default",
        }
    }
}

# TORTOISE = {
#     "connections": {
#         "default": {
#             "engine": "tortoise.backends.asyncpg",
#             "credentials": {
#                 "host": "host_address",
#                 "user": "username",
#                 "password": "password",
#                 "database": "db_name",
#                 "port": 5432,
#             }
#         }
#     },
#     "apps": {
#         "models": {
#             "models": [
#                 "models.misc",
#                 "models",
#                 "aerich.models"
#             ],
#             "default_connection": "default",
#         }
#     }
# }

EXTENSIONS = [
    "cogs.esports",
    "cogs.events",
    "cogs.mod",
    "cogs.premium",
    "cogs.quomisc",
    "cogs.reminder",
    "cogs.utility",
]


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

COLOR = int(os.getenv("COLOR", "0x00FFB3"), 16)
FOOTER = os.getenv("FOOTER", "TOURNEY - BY UBO OFFICIAL!!!")
PREFIX = os.getenv("PREFIX", "u")
PRIME_EMOJI = os.getenv("PRIME_EMOJI", "⚡")
OWNER_ID = os.getenv("OWNER_ID", "1193141979375210546")
DEVS = [int(id.strip()) for id in os.getenv("DEVS", "1193141979375210546").split(",")]

SERVER_LINK = os.getenv("SERVER_LINK", "https://discord.gg/Ex2Y8j3BCm")
SERVER_ID = int(os.getenv("SERVER_ID", "1448359837116403867"))
TOURNEY_CSV_CHANNEL = int(os.getenv("TOURNEY_CSV_CHANNEL", "1448494213879566529"))
EMOJIS_SERVER = [int(id.strip()) for id in os.getenv("EMOJIS_SERVER", "1497971881834451149, 1497972243848757310, 1448359837116403867").split(",")] #atleast 2 server id required...

BOT_INVITE = os.getenv("BOT_INVITE", "....")

ACTIVITIES = [
    {"type": "playing", "name": "scrims across {servers} servers"},
    {"type": "listening", "name": "strategic calls from {members} players"},
    {"type": "watching", "name": "tournament brackets update in real time"},
    {"type": "competing", "name": "to lead the eSports automation arena"},
    {"type": "streaming", "name": "live event analytics", "url": "https://twitch.tv/SACHINBOT"},
]

# ─────────────────────────────────────────────────────────────
#  Activity Placeholders (usable in "name" field)
#  These will automatically update with live bot stats.
#
#  Available Placeholders:
#    {servers}   → Total number of servers the bot is in
#    {members}   → Sum of all members across all servers
#    {msgs}      → Total messages seen since startup
#    {uptime}    → Current uptime in human-readable format
#    {cmds}      → Total commands executed since startup
#
#  Example:
#    {"type": "playing", "name": "serving {servers} communities"}
# ─────────────────────────────────────────────────────────────


# LOGS
SHARD_LOG = os.getenv("SHARD_LOG", "...")
ERROR_LOG = os.getenv("ERROR_LOG", "...")
PUBLIC_LOG = os.getenv("PUBLIC_LOG", "...")



# IGNORE RIGHT NOW
WEBSITE = os.getenv("WEBSITE", "https://tourneybot.xyz")
REPOSITORY = os.getenv("REPOSITORY", "https://github.com/ubosachin/tourney")
FASTAPI_URL = os.getenv("FASTAPI_URL", "https://ocr.gfxvisual.xyz")
FASTAPI_KEY = os.getenv("FASTAPI_KEY", "cyclonestrongsecret")
