import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "26827561"))
API_HASH = getenv("API_HASH", "acb22d6ded8f970b2034135f68d77514")
BOT_TOKEN = getenv("BOT_TOKEN", "5882596610:AAFK_xlHGl_06sdn5fPpiqLqCjn7pjRsUMQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "1BJWap1sBu2xDQJPyAFaM6Y9ftP6zrUU6ne4zrJFmHYWFj84jVk2-qZc5FZGGQWDMC4ss1h_I-nkxd09oAMLfiY8Ks5lE6RLfg5cx0Z5lZgeQPXWi7KL_JZ1PK_ybSdHu-9xQPzlYKxqEPM4jgtidFdY98gyWruqg54Q4YGvEk0Xf-m1_flgioivaFNTiQFKWikp3ajkY5YoQnjV6pLQr9LF9FMtFngnjg854M_XivFM4nPZOADKNs19VA1pbMiW5Ik_mwP7GGT5EUV2s49t26y23ujDgWEZzP-qe9kiQO4IjgPRHB8WVEMTyHvLhuZRxMtlgzPkC_HyzR_OEoNv9z5sn6Aw0QyY=")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
