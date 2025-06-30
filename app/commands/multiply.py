# app/commands/multiply.py
from decimal import Decimal
from app.operations import multiply
from app.command import Command


class MultiplyCommand(Command):
    def __init__(self, value1: Decimal = None, value2: Decimal = None):
        self.value1 = value1
        self.value2 = value2

    def name(self) -> str:
        return "multiply"

    def execute(self, a: str, b: str) -> Decimal:
        return multiply(Decimal(a), Decimal(b))
