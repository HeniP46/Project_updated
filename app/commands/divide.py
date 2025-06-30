from decimal import Decimal
from app.operations import divide


class DivideCommand:
    def __init__(self, value1: Decimal = None, value2: Decimal = None):
        self.value1 = value1
        self.value2 = value2

    def name(self):
        return "divide"

    def execute(self, val1=None, val2=None):
        if val1 is not None and val2 is not None:
            if Decimal(str(val2)) == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return divide(Decimal(str(val1)), Decimal(str(val2)))
        elif self.value1 is not None and self.value2 is not None:
            if self.value2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return divide(self.value1, self.value2)
        else:
            raise ValueError("Values must be provided either in constructor or execute method")
