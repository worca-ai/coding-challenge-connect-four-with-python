import unittest
from connect_four import ConnectFour

class TestConnectFour(unittest.TestCase):
    def test_initial_board(self):
        game = ConnectFour()
        self.assertEqual(len(game.board), 6)
        self.assertEqual(len(game.board[0]), 7)

    def test_drop_piece(self):
        game = ConnectFour()
        game.drop_piece(0)
        self.assertEqual(game.board[-1][0], 'x')

    def test_switch_player(self):
        game = ConnectFour()
        game.switch_player()
        self.assertEqual(game.current_player, 'o')

    # Additional tests for win conditions can be added here

if __name__ == "__main__":
    unittest.main()
