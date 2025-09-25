class Position:
    def __init__(self, x: int, y: int):
        if x < 0 or y < 0:
            raise ValueError("Row and column indices must be non-negative")
        self.x = x
        self.y = y