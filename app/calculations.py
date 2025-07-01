from typing import List, Optional
from app.calculation import Calculation

class Calculations:
    """
    A class to manage a collection (history) of Calculation objects.
    """
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """
        Add a Calculation instance to the history.
        """
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """
        Return the full list of stored Calculation instances.
        """
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        """
        Clear all stored Calculation instances from history.
        """
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Optional[Calculation]:
        """
        Return the most recent Calculation if available, else None.
        """
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """
        Return all Calculation instances with an operation matching the given name.
        """
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
