"""
Sample tests.
"""
from django.test import SimpleTestCase

from app import calc  # type: ignore

class CalcTests(SimpleTestCase):
    """Test the Calc module."""

    def test_add_numbers(self):
        """Test adding numbers."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Test substracting numbers."""
        res = calc.substract(10, 15)

        self.assertEqual(res, 5)
