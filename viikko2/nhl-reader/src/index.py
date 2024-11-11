import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = requests.get(url).json()

    def get_players(self):
        self.players = []
        for player_dict in self.url:
            player = Player(player_dict)
            self.players.append(player)
        return self.players

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        self.players_by_nationality = []
        for player in self.players:
            if player.nationality==nationality:
                self.players_by_nationality.append(player)
        self.sorted = sorted(self.players_by_nationality, key=lambda player: player.points, reverse=True)
        return self.sorted

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
