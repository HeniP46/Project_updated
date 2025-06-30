from app.operations import add
from decimal import Decimal

class AddCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.a = a
        self.b = b
    
    def execute(self):
        return add(self.a, self.b)
