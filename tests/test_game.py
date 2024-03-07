import pytest
from lemon_tictactoe import TicTacToeGame, CellOccupiedError, WrongPlayerError

def test_set_player_name():
    game = TicTacToeGame()

    assert game.players[1] == "Player 1"
    assert game.players[2] == "Player 2"

    game.set_player_name(1, "Bert")
    game.set_player_name(2, "Bob")

    assert game.players[1] == "Bert"
    assert game.players[2] == "Bob"

    with pytest.raises(ValueError) as context:
        game.set_player_name(0, "Berta")
    assert "player_number has to be a value between 1 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        game.set_player_name(3, "Berta")
    assert "player_number has to be a value between 1 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        game.set_player_name(1, 53) #type: ignore
    assert "name has to be of type str" in str(context.value)

def test_set_player_names():
    game = TicTacToeGame()

    game.set_player_names(["Bert", "Bob"])
    assert game.players[1] == "Bert"
    assert game.players[2] == "Bob"

    game.set_player_names(["Bob"])
    assert game.players[1] == "Bob"
    assert game.players[2] == "Bob"

    with pytest.raises(ValueError) as context:
        game.set_player_names(["Bob", "Bert", "Berta"])
    assert "length of player_names can only have a maximum value of 2" in str(context.value)

def test_move():
    game = TicTacToeGame()

    game.move(1, 0, 0)
    assert game._board._grid[0][0] == 1

    game.move(2, 0, 1)
    assert game._board._grid[0][1] == 2

    game.move(1, 1, 0)
    assert game._board._grid[1][0] == 1

    with pytest.raises(WrongPlayerError):
        game.move(1, 1, 1)
    with pytest.raises(CellOccupiedError):
        game.move(2, 1, 0)

    with pytest.raises(ValueError) as context:
        game.move(2, -1, 1)
    assert "x has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        game.move(2, 3, 1)
    assert "x has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        game.move(2, 1, -1)
    assert "y has to be a value between 0 and 2" in str(context.value)

    with pytest.raises(ValueError) as context:
        game.move(2, 1, 3)
    assert "y has to be a value between 0 and 2" in str(context.value)

def test_example_game():
    game = TicTacToeGame()

    assert game._started == False
    assert game._finished == False

    assert game.move(1, 0, 0) == False
    assert game._started == True
    assert game.move(2, 0, 2) == False
    assert game.move(1, 1, 1) == False
    assert game.move(2, 1, 2) == False
    assert game.move(1, 2, 2) == True

    assert game.winner == 1
    assert game._finished == True