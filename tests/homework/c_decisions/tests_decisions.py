import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    def test_options_ratio(self):
        self.assertEqual(get_options_ratio(10,20), .5)
    
    def test_faculty_rating(self):
        self.assertEqual(get_faculty_rating(.91), 'Excellent')