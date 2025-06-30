from decimal import Decimal
from app.operations import add

class AddCommand:
    def __init__(self, value1: Decimal, value2: Decimal):
        self.value1 = value1
        self.value2 = value2

    def execute(self):
        return add(self.value1, self.value2)

