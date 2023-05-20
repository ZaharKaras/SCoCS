from controller import Controller
import sys

class CLI:
    def __init__(self, controller, username):
        self.controller = controller
        self.username = username
        self.commands = {
            "add": self.controller.container.add,
            "remove": self.controller.container.remove,
            "find": self.controller.container.find,
            "list": self.controller.container.list,
            "grep": self.controller.container.grep,
            "save": self.controller.container.save,
            "load": self.controller.container.load,
            "switch": self.controller.container.switch,
            "help": self.print_help,
            "exit": self.exit
        }

    def print_help(self):
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")

    def exit(self):
        print("Exiting program...")
        sys.exit()

    def run(self):
        print(f"Welcome, {self.username}!")
        self.print_help()
        while True:
            command = input("> ").split()
            if not command:
                continue

            action = command[0]
            args = command[1:]

            if action not in self.commands:
                print("Invalid command")
                continue
            elif action == "switch" or action == "remove" or action == "grep":
                if len(args) != 1:
                    print("Error: switch command requires exactly one argument")
                    continue
            elif action == "help" or action == "list" or action == "exit" or action == "load" or action == "save":
                if len(args) != 0:
                    print("Error: switch command requires exactly no one argument")
                    continue



            self.commands[action](*args)