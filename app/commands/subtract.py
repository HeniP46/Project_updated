from decimal import Decimal
from app.operations import subtract
from app.command import Command


class SubtractCommand(Command):
    def __init__(self, value1: Decimal = None, value2: Decimal = None):
        self.value1 = value1
        self.value2 = value2

    def name(self) -> str:
        return "subtract"

    def execute(self, a: str, b: str) -> Decimal:
        return subtract(Decimal(a), Decimal(b))
