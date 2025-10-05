from sudoku.v2.cell import Cell
from sudoku.v2.position import Position


class Block:

    def __init__(self, size: int, cells: list[list[Cell]]):
        Block.__check_size(size)
        Block.__check_cells(cells, size)

        self.size = size
        self.cells = cells

    def at(self, pos: Position) -> Cell:
        self.__check_position(pos)
        return self.cells[pos.y][pos.x]

    def put(self, pos: Position, n: int):
        self.__check_position(pos)
        self.__check_num(n)
        self.cells[pos.y][pos.x].value = n

    def __check_position(self, pos: Position):
        if self.size <= pos.x or self.size <= pos.y:
            raise ValueError("Block position out of bounds for the given size")

    def __check_num(self, n: int):
        if n < 0 or self.size < n:
            raise ValueError(f"Value must be between 0 and {self.size}")

    @staticmethod
    def create_empty(size: int):
        Block.__check_size(size)
        return Block(
            size,
            [[Cell(0) for x in range(size)] for y in range(size)],
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
