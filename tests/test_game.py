# tests/test_game.py
from tictactoe.game import Game


def test_empty_board_not_finished():
    game = Game()
    assert game.check_finish() == -1


def test_horizontal_win():
    game = Game()
    game.move((0, 0), 1)
    game.move((0, 1), 1)
    game.move((0, 2), 1)
    assert game.check_finish() == 1


def test_vertical_win():
    game = Game()
    game.move((0, 0), 2)
    game.move((1, 0), 2)
    game.move((2, 0), 2)
    assert game.check_finish() == 2


def test_diagonal_win():
    game = Game()
    game.move((0, 0), 1)
    game.move((1, 1), 1)
    game.move((2, 2), 1)
    assert game.check_finish() == 1


def test_draw():
    game = Game()
    moves = [
        ((0, 0), 1), ((0, 1), 2), ((0, 2), 1),
        ((1, 0), 1), ((1, 1), 1), ((1, 2), 2),
        ((2, 0), 2), ((2, 1), 1), ((2, 2), 2),
    ]
    for pos, player in moves:
        game.move(pos, player)

    assert game.check_finish() == 0


def test_invalid_move_out_of_range():
    game = Game()
    assert not game.move((3, 3), 1)
    assert not game.move((-1, 0), 1)


def test_invalid_player():
    game = Game()
    assert not game.move((0, 0), 3)
    assert not game.move((0, 0), -1)


def test_remove_move():
    game = Game()
    game.move((1, 1), 1)
    assert game.board[1][1] == 1
    game.move((1, 1), 0)
    assert game.board[1][1] == 0
