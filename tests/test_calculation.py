from decimal import Decimal
import pytest
from app.calculation import Calculation
from app.operations import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, op, expected",
    [
        (Decimal("10"), Decimal("5"), add, Decimal("15")),
        (Decimal("9"), Decimal("3"), divide, Decimal("3")),
        (Decimal("2"), Decimal("3"), add, Decimal("5")),
        (Decimal("6"), Decimal("2"), divide, Decimal("3")),
        (Decimal("10"), Decimal("5"), subtract, Decimal("5")),
        (Decimal("4"), Decimal("3"), multiply, Decimal("12")),
    ],
)
def test_calculation_operations(a, b, op, expected):
    calc = Calculation(a, b, op)
    assert calc.perform() == expected


def test_calculation_repr():
    calc = Calculation(Decimal("10"), Decimal("5"), add)
    assert repr(calc) == "Calculation(10, 5, add)"


def test_divide_by_zero():
    calc = Calculation(Decimal("10"), Decimal("0"), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
