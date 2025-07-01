from decimal import Decimal
from typing import Callable
from app.calculations import Calculations
from app.calculation import Calculation
from app.operations import add, subtract, multiply, divide

class Calculator:
    """
    A Calculator class that performs arithmetic operations
    and records calculations in the history.
    """

    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        Calculations.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition and record the operation."""
        return Calculator._perform_operation(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction and record the operation."""
        return Calculator._perform_operation(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication and record the operation."""
        return Calculator._perform_operation(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division and record the operation."""
        return Calculator._perform_operation(a, b, divide)
