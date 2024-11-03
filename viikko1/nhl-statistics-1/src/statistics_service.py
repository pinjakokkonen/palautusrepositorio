from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, playerReader):
        self._players = playerReader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=None):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            if sort_by==SortBy.GOALS:
                return player.goals
            elif sort_by==SortBy.ASSISTS:
                return player.assists
            else:
                return player.points
            
        if sort_by==None:
            sort_by==1

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
