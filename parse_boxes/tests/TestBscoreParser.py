import unittest
from .my_funs import *

class BoxScoreParserTestCase(unittest.TestCase):
    """Tests for BoxScoreParser class"""

    def test_smoke_test(self):
        self.assertTrue(True)

    def test_add_one(self):
        self.assertEqual(add_one(0), 1)
