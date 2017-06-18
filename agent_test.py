"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

from importlib import reload
import unittest
import sys

import isolation
import game_agent

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.MinimaxPlayer()
        self.player1.time_left = lambda: 30000
        self.player1.score = lambda x,y: float('-inf')
        self.player2 = game_agent.MinimaxPlayer()
        self.player2.time_left = lambda: 30000
        self.player2.score = lambda x,y: float('-inf')
        self.game = isolation.Board(self.player1, self.player2)

    def test_minimax(self):
        print(self.player1.minimax(self.game, 3))

class AlphabetaTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player1.time_left = lambda: 30000
        self.player1.score = lambda x,y: float('-inf')
        self.player2 = game_agent.AlphaBetaPlayer()
        self.player2.time_left = lambda: 30000
        self.player2.score = lambda x,y: float('-inf')
        self.game = isolation.Board(self.player1, self.player2)

    def test_alphabeta(self):
        print(self.player1.alphabeta(self.game, 3))



if __name__ == '__main__':
    unittest.main()
