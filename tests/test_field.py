import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src', 'python')))

from sudoku.field import Field
import unittest

class TestField(unittest.TestCase):
	def test_init_valid(self):
		field = Field([[0]*9 for _ in range(9)])
		self.assertIsInstance(field, Field)

	def test_init_invalid_size(self):
		with self.assertRaises(ValueError):
			Field([[0]*8 for _ in range(9)])  # 8 columns instead of 9

	def test_init_invalid_value(self):
		with self.assertRaises(ValueError):
			Field([[0]*9 for _ in range(8)] + [[10]*9])  # Value out of range

	def test_str_representation(self):
		field = Field([[1, 2, 3, 4, 5, 6, 7, 8, 9]]*9)
		expected_str = (
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"- - - + - - - + - - -\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"- - - + - - - + - - -\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9\n"
			"1 2 3 | 4 5 6 | 7 8 9"
		)
		self.assertEqual(str(field), expected_str)
