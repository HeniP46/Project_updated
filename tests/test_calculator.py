"""
Unit tests for the Calculator class arithmetic methods.
"""

from app.calculator import Calculator


def test_addition():
    """Test addition works."""
    assert Calculator.add(2, 2) == 4


def test_subtraction():
    """Test subtraction works."""
    assert Calculator.subtract(2, 2) == 0


def test_divide():
    """Test division works."""
    assert Calculator.divide(2, 2) == 1


def test_multiply():
    """Test multiplication works."""
    assert Calculator.multiply(2, 2) == 4
