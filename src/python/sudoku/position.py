class Position:

    def __init__(self, row: int, col: int):
        if not (0 <= row < 9) or not (0 <= col < 9):
            raise ValueError("Row and column must be between 0 and 8.")
        self.row = row
        self.col = col

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"Position(row={self.row}, col={self.col})"
