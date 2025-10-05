from sudoku.v2.field import Field
from sudoku.v2.block import Block
from sudoku.v2.position import Position
import util


def start_interactive(size: int) -> Field:
    field = Field.create_empty(size)

    for y in range(field.max_num):
        line = input(f"type the {util.ordinal(y+1)} row separated by comma:")
        nums = [int(n) if n else 0 for n in line.split(",")]
        if len(nums) != field.max_num:
            raise ValueError(f"Expected {field.max_num} numbers, got {len(nums)}")
        for x in range(field.block_size):
            field.put(Position(x, y), nums[x])

    return field


def from_string(size: int, s: str) -> Field:
    field = Field.create_empty(size)

    lines = s.strip().split("\n")
    if len(lines) != field.max_num:
        raise ValueError(f"Expected {field.max_num} lines, got {len(lines)}")

    for y in range(field.max_num):
        nums = [int(n) if n else 0 for n in lines[y].split(",")]
        if len(nums) != field.max_num:
            raise ValueError(f"Expected {field.max_num} numbers, got {len(nums)}")
        for x in range(field.block_size):
            field.put(Position(x, y), nums[x])

    return field
