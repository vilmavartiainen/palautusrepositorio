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
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search(self):
        pelaaja = self.stats.search("Semenko")

        self.assertEqual(str(pelaaja), "Semenko EDM 4 + 12 = 16")

    def test_team(self):
        tiimi = self.stats.team("EDM")

        self.assertEqual(len(tiimi),3)

    def test_top(self):
        toplista = self.stats.top(3)

        self.assertEqual(toplista[0].name, "Gretzky")
        self.assertEqual(toplista[1].name, "Lemieux")

    def test_nimeton(self):
        nimeton = self.stats.search("Koira")

        self.assertEqual(nimeton, None)