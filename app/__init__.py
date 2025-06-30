from app.plugin_loader import load_commands
from app import plugin_loader  # Add this line to expose plugin_loader module

class App:
    @staticmethod
    def start() -> None:
        commands = load_commands()
        print("Welcome to the calculator REPL!")
        print("Available commands:", ", ".join(commands.keys()))
        print("Type 'menu' to show commands again, or 'exit' to quit.")
        
        while True:
            user_input = input(">>> ").strip()
            if user_input == "":
                print("Please enter a command.")
                continue
                
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            elif user_input.lower() == "menu":
                print("Available commands:", ", ".join(commands.keys()))
                continue
                
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Usage: <num1> <num2> <operation>")
                continue
                
            a, b, command_name = parts
            command = commands.get(command_name)
            if command is None:
                print(f"Unknown command: {command_name}")
                continue
                
            try:
                result = command.execute(a, b)
                print(f"Result: {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error: {e}")

# Make both App and plugin_loader available for import
__all__ = ['App', 'plugin_loader']# Make calculator a package
