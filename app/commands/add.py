from decimal import Decimal
from app.operations import add
from app.command import Command


class AddCommand(Command):
    def __init__(self, value1: Decimal = None, value2: Decimal = None):
        self.value1 = value1
        self.value2 = value2

    def name(self) -> str:
        return "add"

    def execute(self, a: str, b: str) -> Decimal:
        return add(Decimal(a), Decimal(b))
