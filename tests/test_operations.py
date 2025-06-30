"""
Tests for individual operations via the Calculation class.
"""

import pytest
from decimal import Decimal
from app.calculation import Calculation
from app.operations import add, subtract, multiply, divide


def test_operation(a, b, operation, expected):
    """Test Calculation.perform with various operations."""
    calc = Calculation.create(a, b, operation)
    assert calc.perform() == expected


def test_divide_by_zero():
    """Test dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = Calculation(Decimal('10'), Decimal('0'), divide)
        calc.perform()
