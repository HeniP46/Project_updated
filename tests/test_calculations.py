"""
Tests for the Calculations history class.
"""

from decimal import Decimal
import pytest
from app.calculation import Calculation
from app.calculations import Calculations
from app.operations import add, subtract


@pytest.fixture
def setup_calculations():
    """Fixture to clear and initialize calculation history."""
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))


def test_add_calculation(setup_calculations):
    """Test adding a calculation to the history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc


def test_get_history(setup_calculations):
    """Test retrieving the entire calculation history."""
    history = Calculations.get_history()
    assert len(history) == 2


def test_clear_history(setup_calculations):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0


def test_get_latest(setup_calculations):
    """Test getting the latest calculation."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3')


def test_find_by_operation(setup_calculations):
    """Test finding calculations by operation type."""
    adds = Calculations.find_by_operation("add")
    subs = Calculations.find_by_operation("subtract")
    assert len(adds) == 1
    assert len(subs) == 1


def test_get_latest_with_empty_history():
    """Test getting latest from empty history returns None."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None
