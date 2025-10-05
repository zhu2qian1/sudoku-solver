from unittest import TestCase
import util

class TestUtil(TestCase):

    def test_ordinal(self):
        self.assertEqual(util.ordinal(1), "1st")
        self.assertEqual(util.ordinal(2), "2nd")
        self.assertEqual(util.ordinal(3), "3rd")
        self.assertEqual(util.ordinal(4), "4th")
        self.assertEqual(util.ordinal(10), "10th")
        self.assertEqual(util.ordinal(11), "11th")
        self.assertEqual(util.ordinal(12), "12th")
        self.assertEqual(util.ordinal(13), "13th")
        self.assertEqual(util.ordinal(21), "21st")
        self.assertEqual(util.ordinal(22), "22nd")
        self.assertEqual(util.ordinal(23), "23rd")
        self.assertEqual(util.ordinal(101), "101st")
        self.assertEqual(util.ordinal(111), "111th")
        self.assertEqual(util.ordinal(0), "0th")
        self.assertEqual(util.ordinal(-1), "-1st")
        self.assertEqual(util.ordinal(-2), "-2nd")
        self.assertEqual(util.ordinal(-3), "-3rd")
        self.assertEqual(util.ordinal(-4), "-4th")
        self.assertEqual(util.ordinal(-11), "-11th")
        self.assertEqual(util.ordinal(-21), "-21st")
        self.assertEqual(util.ordinal(-22), "-22nd")
        self.assertEqual(util.ordinal(-23), "-23rd")
        self.assertEqual(util.ordinal(-101), "-101st")
        self.assertEqual(util.ordinal(-111), "-111th")

    def test_ordinal_non_integer(self):
        with self.assertRaises(TypeError):
            util.ordinal(1.5)
        with self.assertRaises(TypeError):
            util.ordinal("1")
        with self.assertRaises(TypeError):
            util.ordinal(None)

    def test_with_custom_integer_type(self):
        class CustomInt(int):
            pass

        self.assertEqual(util.ordinal(CustomInt(1)), "1st")
        self.assertEqual(util.ordinal(CustomInt(2)), "2nd")
        self.assertEqual(util.ordinal(CustomInt(3)), "3rd")
        self.assertEqual(util.ordinal(CustomInt(4)), "4th")
        self.assertEqual(util.ordinal(CustomInt(11)), "11th")
        self.assertEqual(util.ordinal(CustomInt(21)), "21st")
        self.assertEqual(util.ordinal(CustomInt(-1)), "-1st")
        self.assertEqual(util.ordinal(CustomInt(-11)), "-11th")
