import unittest

from src.examples.c_decisions.decisions import is_letter_consonant, logical_op_precedence, num_is_not_in_range_or, number_is_in_range_and, test_config
from src.examples.c_decisions.decisions import get_letter_grade
from src.examples.c_decisions.decisions import logical_op_precedence
from src.examples.c_decisions.decisions import number_is_not_in_range

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_get_letter_grade(self):
        self.assertEqual('A', get_letter_grade(90))
        self.assertEqual('B', get_letter_grade(85))
        self.assertEqual('C', get_letter_grade(75))
        self.assertEqual('D', get_letter_grade(65))
        self.assertEqual('F', get_letter_grade(55))
        self.assertEqual('Invalid Number', get_letter_grade(-10))
    
    def test_logical_op_precedence(self):
        self.assertEqual(True, logical_op_precedence(True, False, True))
        self.assertEqual(False, logical_op_precedence(False, False, False))

    def test_number_is_in_range(self):
        self.assertEqual(True, number_is_in_range_and(20, 100, 50))
        self.assertEqual(False, number_is_in_range_and(20, 100, 0))
        self.assertEqual(True, number_is_in_range_and(20, 100, 100))
        self.assertEqual(False, number_is_in_range_and(20, 100, 101))

    def test_number_is_not_in_range(self):
        self.assertEqual(True, number_is_not_in_range(20, 100, 101))
        self.assertEqual(True, number_is_not_in_range(20, 100, 50))

    def test_num_is_not_in_range_or(self):
        self.assertEqual(True, num_is_not_in_range_or(20, 100, 101))
        self.assertEqual(False, num_is_not_in_range_or(20, 100, 50))
    
    def test_is_letter_consonant(self):
        self.assertEqual(False, is_letter_consonant('a'))
        self.assertEqual(True, is_letter_consonant('z'))