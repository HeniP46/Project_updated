"""
Tests for individual operations via the Calculation class.
"""
import pytest
from decimal import Decimal
from app.calculation import Calculation
from app.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "val1, val2, op, result",
    [
        (Decimal("10"), Decimal("5"), add, Decimal("15")),
        (Decimal("10"), Decimal("5"), subtract, Decimal("5")),
        (Decimal("10"), Decimal("5"), multiply, Decimal("50")),
        (Decimal("10"), Decimal("5"), divide, Decimal("2")),
        (Decimal("9"), Decimal("3"), divide, Decimal("3")),
        (Decimal("2"), Decimal("3"), add, Decimal("5")),
        (Decimal("8"), Decimal("2"), subtract, Decimal("6")),
        (Decimal("3"), Decimal("4"), multiply, Decimal("12")),
    ],
)
def test_operation(val1, val2, op, result):
    """Test Calculation.perform with various operations."""
    calc = Calculation.create(val1, val2, op)
    assert calc.perform() == result


def test_divide_by_zero():
    """Test dividing by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc = Calculation(Decimal('10'), Decimal('0'), divide)
        calc.perform()
