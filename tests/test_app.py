"""Test suite for the App REPL interface."""
import pytest
from app import App


def test_app_start_exit_command(capfd, monkeypatch):
    """Test that entering 'exit' exits the application."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, _ = capfd.readouterr()
    assert "Welcome to the calculator REPL!" in out
    assert "Exiting..." in out


def test_app_start_unknown_command_then_exit(capfd, monkeypatch):
    """Test unknown command followed by 'exit'."""
    inputs = iter(['foo', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Unknown command" in out or "Invalid input" in out
    assert "Exiting..." in out


def test_app_menu_command(capfd, monkeypatch):
    """Test that 'menu' displays available commands."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Available commands:" in out
    assert "Exiting..." in out


def test_app_invalid_format(capfd, monkeypatch):
    """Test input with invalid format."""
    inputs = iter(['5 +', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Invalid input. Usage" in out
    assert "Exiting..." in out


def test_app_valid_add_command(capfd, monkeypatch):
    """Test a valid add command."""
    inputs = iter(['5 3 add', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Result: 8" in out
    assert "Exiting..." in out


def test_app_command_with_invalid_number(capfd, monkeypatch):
    """Test non-numeric input for calculation."""
    inputs = iter(['abc 5 add', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error:" in out
    assert "Exiting..." in out


def test_app_divide_by_zero(capfd, monkeypatch):
    """Test division by zero handling."""
    inputs = iter(['5 0 divide', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Error: Cannot divide by zero" in out
