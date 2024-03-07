import pytest
from lemon_tictactoe import CellOccupiedError
from lemon_tictactoe.game.board import Board

def test_init():
    board = Board(size=100)

    assert board.size == 100
    assert len(board._grid) == 100
    for row in board._grid:
        assert len(row) == 100

    board = Board(size=3, player_count=2)
    assert board.size == 3

    assert len(board._row_counts) == 3
    for row in board._row_counts:
        assert len(row) == 2
        assert row[1] == 0
        assert row[2] == 0

    assert len(board._column_counts) == 3
    for column in board._column_counts:
        assert len(column) == 2
        assert column[1] == 0
        assert column[2] == 0

    assert len(board._bottomleft_topright) == 2
    assert board._bottomleft_topright[1] == 0
    assert board._bottomleft_topright[2] == 0

    assert len(board._topleft_bottomright) == 2
    assert board._topleft_bottomright[1] == 0
    assert board._topleft_bottomright[2] == 0

def test_validate_coordinates():
    board = Board(size=3, player_count=2)

    assert board._validate_coordinates(0, 0) is None

    with pytest.raises(ValueError) as context:
        board._validate_coordinates(-1, 1)
    assert "x has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        board._validate_coordinates(3, 1)
    assert "x has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        board._validate_coordinates(1, -1)
    assert "y has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        board._validate_coordinates(1, 3)
    assert "y has to be a value between 0 and 2" in str(context.value)

def test_place():
    board = Board(size=3, player_count=2)

    board._place(1, 0, 0)
    assert board._grid[0][0] == 1

    board._place(2, 0, 1)
    assert board._grid[0][1] == 2

    board._place(1, 1, 0)
    assert board._grid[1][0] == 1

    with pytest.raises(CellOccupiedError):
        board._place(2, 1, 0)

def test_add_row_count():
    board = Board(size=3, player_count=2)

    assert board._add_row_count(row=0, player_number=1) is False
    assert board._add_row_count(row=0, player_number=1) is False
    assert board._add_row_count(row=0, player_number=1) is True

def test_add_column_count():
    board = Board(size=3, player_count=2)

    assert board._add_column_count(column=0, player_number=1) is False
    assert board._add_column_count(column=0, player_number=1) is False
    assert board._add_column_count(column=0, player_number=1) is True

def test_add_bottomleft_topright():
    board = Board(size=3, player_count=2)

    assert board._add_bottomleft_topright(player_number=1) is False
    assert board._add_bottomleft_topright(player_number=1) is False
    assert board._add_bottomleft_topright(player_number=1) is True

def test_add_topleft_bottomright():
    board = Board(size=3, player_count=2)

    assert board._add_topleft_bottomright(player_number=1) is False
    assert board._add_topleft_bottomright(player_number=1) is False
    assert board._add_topleft_bottomright(player_number=1) is True

def test_count_win_condition():
    board = Board(size=3, player_count=2)

    assert board._count_win_condition(1, 0, 0) is False
    assert board._row_counts == [{1: 1, 2: 0}, {1: 0, 2: 0}, {1: 0, 2: 0}]
    assert board._column_counts == [{1: 1, 2: 0}, {1: 0, 2: 0}, {1: 0, 2: 0}]
    assert board._topleft_bottomright == {1: 1, 2: 0}
    assert board._bottomleft_topright == {1: 0, 2: 0}

    assert board._count_win_condition(1, 1, 1) is False
    assert board._row_counts == [{1: 1, 2: 0}, {1: 1, 2: 0}, {1: 0, 2: 0}]
    assert board._column_counts == [{1: 1, 2: 0}, {1: 1, 2: 0}, {1: 0, 2: 0}]
    assert board._topleft_bottomright == {1: 2, 2: 0}
    assert board._bottomleft_topright == {1: 1, 2: 0}

    assert board._count_win_condition(1, 2, 2) is True
    assert board._row_counts == [{1: 1, 2: 0}, {1: 1, 2: 0}, {1: 1, 2: 0}]
    assert board._column_counts == [{1: 1, 2: 0}, {1: 1, 2: 0}, {1: 1, 2: 0}]
    assert board._topleft_bottomright == {1: 3, 2: 0}
    assert board._bottomleft_topright == {1: 1, 2: 0}