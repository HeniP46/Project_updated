"""Tests for app REPL commands."""
import pytest
from app import App


def test_app_start_exit_command(capfd, monkeypatch):
    """Test starting the app and immediately exiting."""
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    App.start()
    out, _ = capfd.readouterr()
    assert "Welcome to the calculator REPL!" in out
    assert "Exiting..." in out


def test_app_unknown_command_then_exit(capfd, monkeypatch):
    """Test unknown command input followed by exit."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    App.start()
    out, _ = capfd.readouterr()
    assert "Invalid input. Usage: <num1> <num2> <operation>" in out
    assert "Exiting..." in out
