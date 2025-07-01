from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    """
    Abstract base class for all command objects that
    perform operations on two string inputs and return a Decimal.
    """

    @abstractmethod
    def name(self) -> str:
        """Return the name of the command."""
        pass

    @abstractmethod
    def execute(self, a: str, b: str) -> Decimal:
        """
        Execute the command using string inputs `a` and `b`.
        Returns:
            Decimal: The result of the operation.
        """
        pass
