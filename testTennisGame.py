import unittest
from TennisGame import TennisGame


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # create a new TennisGame
        game = TennisGame()

        self.assertEqual("love-all", game.scoreString())


if __name__ == '__main__':
    unittest.main()
