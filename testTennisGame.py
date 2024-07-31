import unittest

from TennisGame import TennisGame

PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"


class MyTestCase(unittest.TestCase):
    def test_player1_score(self):
        # create a new TennisGame
        game = TennisGame()
        self.assertEqual("love-all", game.score_string())

        game.score(PLAYER_1)
        self.assertEqual("15-love", game.score_string())

        game.score(PLAYER_1)
        self.assertEqual("30-love", game.score_string())

        game.score(PLAYER_1)
        self.assertEqual("40-love", game.score_string())

        game.score(PLAYER_1)
        self.assertEqual("Player 1 win.", game.score_string())

    def test_player2_score(self):
        # create a new TennisGame
        game = TennisGame()
        self.assertEqual("love-all", game.score_string())

        game.score(PLAYER_2)
        self.assertEqual("love-15", game.score_string())

        game.score(PLAYER_2)
        self.assertEqual("love-30", game.score_string())

        game.score(PLAYER_2)
        self.assertEqual("love-40", game.score_string())

        game.score(PLAYER_2)
        self.assertEqual("Player 2 win.", game.score_string())

    def test_xxx_all(self):
        # create a new TennisGame
        game = TennisGame()
        self.assertEqual("love-all", game.score_string())
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        self.assertEqual("15-all", game.score_string())
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        self.assertEqual("30-all", game.score_string())
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        self.assertEqual("40-all", game.score_string())
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        self.assertEqual("Deuce", game.score_string())
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        self.assertEqual("Deuce", game.score_string())

    def test_advance(self):
        # create a new TennisGame
        game = TennisGame()
        game.score(PLAYER_1)
        game.score(PLAYER_1)
        game.score(PLAYER_1)
        game.score(PLAYER_2)
        game.score(PLAYER_2)
        game.score(PLAYER_2)
        self.assertEqual("40-all", game.score_string())
        game.score(PLAYER_1)
        self.assertEqual("%s Advance." % PLAYER_1, game.score_string())
        game.score(PLAYER_2)
        self.assertEqual("Deuce", game.score_string())
        game.score(PLAYER_1)
        self.assertEqual("%s Advance." % PLAYER_1, game.score_string())
        game.score(PLAYER_2)
        self.assertEqual("Deuce", game.score_string())
        game.score(PLAYER_2)
        self.assertEqual("%s Advance." % PLAYER_2, game.score_string())
        game.score(PLAYER_1)
        self.assertEqual("Deuce", game.score_string())
        game.score(PLAYER_2)
        self.assertEqual("%s Advance." % PLAYER_2, game.score_string())

if __name__ == '__main__':
    unittest.main()
