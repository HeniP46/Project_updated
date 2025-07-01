import os
import importlib
from typing import Dict
from app.command import Command

def load_commands() -> Dict[str, Command]:
    """
    Dynamically load command classes from the app/commands directory.

    Returns:
        A dictionary mapping command names to command instances.
    """
    commands = {}
    commands_dir = os.path.join(os.path.dirname(__file__), "commands")

    if not os.path.isdir(commands_dir):
        raise FileNotFoundError(f"Commands directory not found: {commands_dir}")

    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"app.commands.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)

                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if (
                        isinstance(attribute, type)
                        and issubclass(attribute, Command)
                        and attribute is not Command
                    ):
                        instance = attribute()
                        commands[instance.name()] = instance

            except ImportError as e:
                print(f"Warning: Could not import {module_name}: {e}")
                continue
            except Exception as e:
                print(f"Warning: Error loading command from {module_name}: {e}")
                continue

    return commands
