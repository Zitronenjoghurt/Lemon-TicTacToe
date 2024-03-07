from lemon_tictactoe import exceptions
from lemon_tictactoe.utils.validator import validate_in_between

class Board():
    def __init__(self, size: int = 3, player_count: int = 2) -> None:
        self.size = size
        self._grid = [[0]*size for _ in range(size)]

        # WIN CONDITION HANDLING
        # Prevents the use of loops to check win conditions
        self._row_counts = [{i: 0 for i in range(1, player_count + 1)} for _ in range(size)]
        self._column_counts = [{i: 0 for i in range(1, player_count + 1)} for _ in range(size)]
        self._topleft_bottomright = {i: 0 for i in range(1, player_count + 1)}
        self._bottomleft_topright = {i: 0 for i in range(1, player_count + 1)}

    def _place(self, player_number: int, x: int, y: int) -> None:
        self._validate_coordinates(x=x, y=y)
        if self._grid[x][y] != 0:
            raise exceptions.CellOccupiedError(f"Invalid move: cell ({x}, {y}) is already occupied")
        self._grid[x][y] = player_number
        return self._count_win_condition(player_number=player_number, x=x, y=y)

    def _validate_coordinates(self, x: int, y: int) -> None:
        validate_in_between(x, 0, self.size-1, "x")
        validate_in_between(y, 0, self.size-1, "y")

    # Returns true if one of the win conditions is met
    def _count_win_condition(self, player_number: int, x: int, y: int) -> bool:
        win = self._add_column_count(column=x, player_number=player_number)
        if win:
            return True
        
        win = self._add_row_count(row=y, player_number=player_number)
        if win:
            return True
        
        if x == y:
            win = self._add_topleft_bottomright(player_number=player_number)
            if win:
                return True
        
        if x + y == self.size - 1:
            win = self._add_bottomleft_topright(player_number=player_number)
            if win:
                return True
        
        return False

    # Returns true if the win condition is met
    def _add_row_count(self, row: int, player_number: int) -> bool:
        self._row_counts[row][player_number] += 1
        if self._row_counts[row][player_number] == self.size:
            return True
        return False
    
    # Returns true if the win condition is met
    def _add_column_count(self, column: int, player_number: int) -> bool:
        self._column_counts[column][player_number] += 1
        if self._column_counts[column][player_number] == self.size:
            return True
        return False
    
    # Returns true if the win condition is met
    def _add_topleft_bottomright(self, player_number: int) -> bool:
        self._topleft_bottomright[player_number] += 1
        if self._topleft_bottomright[player_number] == self.size:
            return True
        return False
    
    # Returns true if the win condition is met
    def _add_bottomleft_topright(self, player_number: int) -> bool:
        self._bottomleft_topright[player_number] += 1
        if self._bottomleft_topright[player_number] == self.size:
            return True
        return False