from sudoku.position import Position
import unittest

class TestPosition(unittest.TestCase):
	def test_valid_position(self):
		pos = Position(0, 0)
		self.assertEqual(pos.row, 0)
		self.assertEqual(pos.col, 0)

		pos = Position(8, 8)
		self.assertEqual(pos.row, 8)
		self.assertEqual(pos.col, 8)

	def test_invalid_row(self):
		with self.assertRaises(ValueError):
			Position(-1, 0)
		with self.assertRaises(ValueError):
			Position(9, 0)

	def test_invalid_col(self):
		with self.assertRaises(ValueError):
			Position(0, -1)
		with self.assertRaises(ValueError):
			Position(0, 9)

