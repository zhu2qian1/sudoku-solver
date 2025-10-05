from sudoku.v2.cell import Cell
from sudoku.v2.position import Position


class Block:
    def __init__(self, size: int, cells: list[list[Cell]], pos: Position):
        Block.__check_size(size)
        Block.__check_cells(cells, size)
        Block.__check_position(pos, size)

        self.size = size
        self.cells = cells
        self.pos = pos

    def at(self, pos: Position) -> Cell:
        Block.__check_position(pos, self.size)
        return self.cells[pos.y][pos.x]

    @staticmethod
    def create_empty(size: int, pos: Position = Position(0, 0)):
        Block.__check_size(size)
        return Block(
            size,
            [[Cell(Position(x, y)) for x in range(size)] for y in range(size)],
            pos,
        )

    @staticmethod
    def __check_size(size: int):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        if size == 1:
            raise ValueError("Size of 1x1 block is not allowed in Sudoku")

    @staticmethod
    def __check_cells(cells: list[list[Cell]], size: int):
        if len(cells) != size or any(len(row) != size for row in cells):
            raise ValueError("Cells must be a square matrix of the given size")

    @staticmethod
    def __check_position(pos: Position, size: int):
        if pos.x < 0 or pos.y < 0:
            raise ValueError("Block position indices must be non-negative")
        if pos.x >= size or pos.y >= size:
            raise ValueError("Block position out of bounds for the given size")
