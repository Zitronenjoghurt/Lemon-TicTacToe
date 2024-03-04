class CellOccupiedException(Exception):
    """
    Raised when a chosen board cell is already occupied.
    """
    pass

class WrongPlayerException(Exception):
    """
    Raised when the wrong player was chosen for a TicTacToe action.
    """
    pass