import requests
from player import Player

class PlayerReader:
    def __init__(self, season):
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players