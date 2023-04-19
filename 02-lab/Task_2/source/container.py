import re
import json

class SetContainer:
    def __init__(self, user_name: str):
        self.container = set()
        self.current_user = user_name

    def add(self, *keys):
        for key in keys:
            self.container.add(key)

    def remove(self, key):
        self.container.discard(key)

    def find(self, *keys):
        found_keys = [key for key in keys if key in self.container]
        if found_keys:
            print(*found_keys)
        else:
            print("No such elements")

    def list(self):
        for item in self.container:
            print(item)

    def grep(self, regex):
        import re
        found = [elem for elem in self.container if re.match(regex, elem)]
        if found:
            for f in found:
                print(f)
        else:
            print("No such elements")

    def save(self, filename = '/home/karas/studying/4-semester/SCoCS/02-lab/data.json'):
        data = {
        "container": list(self.container),
        "current_user": self.current_user
        }   
        try:
            with open(filename, "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
                existing_data = {}

        existing_data.update(data)
        with open(filename, "w") as f:
            json.dump(existing_data, f, indent=4)

    def load(self, filename = 'data.json'):
        with open(filename, "r") as f:
            data = json.load(f)
        self.container = set(data["container"])
        self.current_user = data["current_user"]

    def switch(self, user):
        self.current_user = user
        print(f"Switched to user {user}")