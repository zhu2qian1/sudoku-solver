from sudoku.v2.position import Position
from sudoku.v2.block import Block


class Field:
    def __init__(self, block_size: int, blocks: list[list[Block]]):
        if block_size <= 0:
            raise ValueError("Block size must be a positive integer")
        if blocks:
            if len(blocks) != block_size or any(
                len(row) != block_size for row in blocks
            ):
                raise ValueError(
                    "Blocks must be a square matrix of the given block size"
                )

        self.block_size = block_size
        self.max_pos = block_size * block_size - 1
        self.blocks = blocks

    @staticmethod
    def create_empty(block_size: int):
        if block_size <= 0:
            raise ValueError("Block size must be a positive integer")
        if block_size == 1:
            raise ValueError("Block size of 1 is not allowed in Sudoku")
        blocks = [
            [Block.create_empty(block_size, Position(x, y)) for x in range(block_size)]
            for y in range(block_size)
        ]
        return Field(block_size, blocks)

    def put(self, pos: Position, n: int):
        self.__check_pos(pos)
        if n < 0 or n > self.max_pos:
            raise ValueError(f"Value must be between 0 and {self.block_size}")
        x = pos.x // self.block_size
        y = pos.y // self.block_size
        bx = pos.x % self.block_size
        by = pos.y % self.block_size
        self.__at_block(Position(x, y)).at(Position(bx, by)).value = n

    def at(self, pos: Position) -> int:
        self.__check_pos(pos)
        x = pos.x // self.block_size
        y = pos.y // self.block_size
        bx = pos.x % self.block_size
        by = pos.y % self.block_size
        return self.__at_block(Position(x, y)).at(Position(bx, by)).value

    def __at_block(self, pos: Position) -> Block:
        self.__check_pos(pos)
        x = pos.x // self.block_size
        y = pos.y // self.block_size
        return self.blocks[y][x]

    def __check_pos(self, pos: Position) -> None:
        if pos.x < 0 or pos.y < 0:
            raise ValueError("Row and column indices must be non-negative")
        if pos.x > self.max_pos or pos.y > self.max_pos:
            raise ValueError(f"Position out of bounds for field size {self.max_pos}")
        return
