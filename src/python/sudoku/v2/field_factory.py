from sudoku.v2.field import Field
from sudoku.v2.position import Position
import util

def start_interactive(size: int) -> Field:
    if size <= 1:
        raise ValueError("Size must be greater than 1")

    field = Field.create_empty(size)

    for y in range(field.block_size**2):
        line = input(f"type the {util.ordinal(y+1)} row separated by comma:")
        nums = [int(n) if n else 0 for n in line.split(",")]
        if len(nums) != field.block_size**2:
            raise ValueError(
                f"Expected {field.block_size**2} numbers, got {len(nums)}"
            )
        for x in range(field.block_size):
            field.put(Position(x, y), nums[x])

    return field

def from_string(size: int, s: str) -> Field:
    if size <= 1:
        raise ValueError("Size must be greater than 1")

    field = Field.create_empty(size)

    lines = s.strip().split("\n")
    if len(lines) != field.block_size**2:
        raise ValueError(f"Expected {field.block_size**2} lines, got {len(lines)}")

    for y in range(field.block_size**2):
        nums = [int(n) if n else 0 for n in lines[y].split(",")]
        if len(nums) != field.block_size**2:
            raise ValueError(
                f"Expected {field.block_size**2} numbers, got {len(nums)}"
            )
        for x in range(field.block_size):
            field.put(Position(x, y), nums[x])

    return field