from decimal import Decimal
from typing import Callable

class Calculation:
    """
    A class to represent a calculation using two Decimal values and an arithmetic operation.
    """

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """
        Static factory method to create a new Calculation instance.
        """
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """
        Executes the arithmetic operation on the two values.
        """
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        """
        Returns a developer-friendly string representation of the Calculation instance.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
