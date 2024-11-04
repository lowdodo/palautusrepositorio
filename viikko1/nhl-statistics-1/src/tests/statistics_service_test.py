import unittest
from statistics_service import StatisticsService, SortBy
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
        self.players = PlayerReaderStub().get_players()

    def test_find_player(self):
        player = self.stats.search("Semenko")
        self.assertAlmostEqual(str(self.players[0]), str(player))

    def test_no_such_player(self):
        player = self.stats.search("Nobody")
        self.assertAlmostEqual(player, None)

    def test_find_team(self):
        team = self.stats.team("EDM")
        teammates = [self.players[0], self.players[2], self.players[4]]
        teammembers = [player.name for player in team]
        teammates = [player.name for player in teammates]
        self.assertAlmostEqual(teammates, teammembers)

    def test_best_points(self):
        best = self.stats.top(1, SortBy.POINTS)
        self.assertAlmostEqual(str(best[0]), str(self.players[4]))


    def test_best_goals(self):
        best = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(str(best[0]), str(self.players[1]))        

    def test_best_assists(self):
        best = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(str(best[0]), str(self.players[4]))
