import json
from steampy.client import SteamClient
from steampy.utils import GameOptions

class SteamLevelUpBot:
    def __init__(self, api_key, username, password, steam_guard_file):
        self.api_key = api_key
        self.username = username
        self.password = password