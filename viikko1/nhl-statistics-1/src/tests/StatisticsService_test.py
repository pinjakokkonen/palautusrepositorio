import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_player_in_players(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_player_not_players(self):
        player = self.stats.search("Temenko")
        self.assertEqual(player, None)

    def test_teams_players_amount(self):
        self.assertAlmostEqual(len(self.stats.team("EDM")), 3)

    def test_top_(self):
        self.assertAlmostEqual(len(self.stats.top(0)), 1)