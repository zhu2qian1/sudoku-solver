import unittest

from sudoku.v2.position import Position
from sudoku.v2.field import Field


class TestV2Field(unittest.TestCase):

    def test_create_empty(self):

        field = Field.create_empty(3)

        self.assertEqual(field.block_size, 3)
        self.assertEqual(field.max_num, 9)

        ids = set()

        for i in range(field.block_size**2):
            ids.add(
                id(
                    field.at_block(
                        Position(i % field.block_size, i // field.block_size)
                    )
                )
            )
            self.assertEqual(len(ids), i + 1)  # all blocks are different id

        for y in range(field.max_num):
            for x in range(field.max_num):
                self.assertEqual(field.at(Position(x, y)).value, 0)
