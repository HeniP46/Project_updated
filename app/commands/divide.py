from decimal import Decimal
from app.operations import divide
from app.command import Command


class DivideCommand(Command):
    def __init__(self, value1: Decimal = None, value2: Decimal = None):
        self.value1 = value1
        self.value2 = value2

    def name(self) -> str:
        return "divide"

    def execute(self, a: str, b: str) -> Decimal:
        if Decimal(b) == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return divide(Decimal(a), Decimal(b))
