class Controller:
    def __init__(self, container):
        self.container = container

    def load_container(self):
        if self.username is not None:
            filename = f"{self.username}.json"
            try:
                self.container.load(filename)
            except FileNotFoundError:
                print(f"Error: could not find file {filename}")
        else:
            print("Error: username is not set")
    
    def parse_command(self, command_str):
        tokens = command_str.strip().split()

        if not tokens:
            # Empty input
            return None, []

        action = tokens[0]
        args = tokens[1:]

        if action == "add":
            # Example usage: "add elem1 elem2 elem3"
            if not args:
                print("Error: add command requires at least one argument")
                return None, []
            for elem in args:
                self.container.add(elem)
            return action, args

        elif action == "remove":
            # Example usage: "remove elem"
            if len(args) != 1:
                print("Error: remove command requires exactly one argument")
                return None, []
            self.container.remove(args[0])
            return action, args

        elif action == "find":
            # Example usage: "find elem1 elem2 elem3"
            if not args:
                print("Error: find command requires at least one argument")
                return None, []
            found = self.container.find(*args)
            if found:
                print("Found elements: ", ", ".join(found))
            else:
                print("No such elements found")
            return action, args

        elif action == "list":
            # Example usage: "list"
            self.container.list()
            return action, args

        elif action == "grep":
            # Example usage: "grep regex"
            if len(args) != 1:
                print("Error: grep command requires exactly one argument")
                return None, []
            found = self.container.grep(args[0])
            if found:
                print("Found elements: ", ", ".join(found))
            else:
                print("No such elements found")
            return action, args

        elif action == "save":
            self.container.save()
            print("Container saved to data.json")
            return action, args

        elif action == "load":
            # Example usage: "load filename"
            if len(args) != 1:
                print("Error: load command requires exactly one argument")
                return None, []
            self.container.load(args[0])
            print("Container loaded from", args[0])
            return action, args

        elif action == "switch":
            # Example usage: "switch username"
            if len(args) != 1:
                print("Error: switch command requires exactly one argument")
                return None, []
            self.container.switch(args[0])
            print("Switched to user", args[0])
            return action, args

        else:
            print("Invalid command:", action)
            return None, []