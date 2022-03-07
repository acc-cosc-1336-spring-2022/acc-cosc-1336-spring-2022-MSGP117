import unittest

from src.examples.d_repetition.repetition import sum_of_squares

class Test_Config(unittest.TestCase):

    def test_sum_of_squares(self):
        self.assertEqual(14, sum_of_squares(3))

    