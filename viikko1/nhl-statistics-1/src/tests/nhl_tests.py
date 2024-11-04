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
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_find_player(self):
        player = self.stats.search("Semenko")
        self.assertAlmostEqual(str(self.players[0]), str(player))

    def test_no_such_player(self):
        player = self.stats.search("Nobody")
        self.assertFalse(player)

    def test_find_tean(self):
        team = self.stats.team("EDM")
        teammates = [self.players[0], self.players[2], self.players[4]]
        self.assertAlmostEquals(team, teammates)
    
