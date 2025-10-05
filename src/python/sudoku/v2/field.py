from sudoku.v2.position import Position
from sudoku.v2.block import Block
from sudoku.v2.cell import Cell


class Field:

    def __init__(self, blocks: list[list[Block]]):
        Field.__check_blocks(blocks)

        block_size = len(blocks)
        self.block_size = block_size
        self.max_pos = block_size**2 - 1
        self.max_num = block_size**2
        self.blocks = blocks

    def put(self, pos: Position, n: int):
        self.__check_pos(pos)
        self.__check_num(n)
        self.at_block(Position(pos.x // self.block_size, pos.y // self.block_size)).at(
            Position(pos.x % self.block_size, pos.y % self.block_size)
        ).value = n

    def at(self, pos: Position) -> Cell:
        self.__check_pos(pos)
        return self.at_block(
            Position(pos.x // self.block_size, pos.y // self.block_size)
        ).at(Position(pos.x % self.block_size, pos.y % self.block_size))

    def at_block(self, pos: Position) -> Block:
        self.__check_pos(pos)
        x = pos.x // self.block_size
        y = pos.y // self.block_size
        return self.blocks[y][x]

    def __check_pos(self, pos: Position) -> None:
        if self.max_pos < pos.x or self.max_pos < pos.y:
            raise ValueError(f"Position out of bounds for field size {self.max_pos}")
        return

    def __check_num(self, n: int) -> None:
        if n < 0 or self.max_num < n:
            raise ValueError(f"Value must be between 0 and {self.max_num}")
        return

    @staticmethod
    def __check_blocks(blocks: list[list[Block]]) -> None:
        if not blocks:
            raise ValueError("Blocks cannot be empty")
        size = len(blocks)
        for row in blocks:
            if not row:
                raise ValueError("Blocks cannot be empty")
            if len(row) != size:
                raise ValueError("Blocks must form a square matrix")
            for block in row:
                if not block:
                    raise ValueError("Blocks cannot be empty")
                if block.size != size:
                    raise ValueError("All blocks must have the same size as the field")
        return

    @staticmethod
    def create_empty(block_size: int):
        Field.__check_size(block_size)
        blocks = list()
        for y in range(block_size):
            row = list()
            for x in range(block_size):
                row.append(Block.create_empty(block_size))
            blocks.append(row)
        return Field(blocks)

    @staticmethod
    def __check_size(size: int):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        if size == 1:
            raise ValueError("Size of 1x1 block is not allowed in Sudoku")
        return
