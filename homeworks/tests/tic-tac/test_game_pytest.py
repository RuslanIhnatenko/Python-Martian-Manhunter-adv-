import pytest
from game import TicTacToe


def setup():
    global game2
    game2 = TicTacToe()
    game2.board[1] = "X"


def test_available_moves():
    assert (1 not in game2.available_moves())


def test_make_move():
    assert not (game2.make_move(1, "X"))
    assert (game2.make_move(3, "X"))
    assert (game2.board[3] != " ")
