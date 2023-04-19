import re
import json

class SetContainer:
    def __init__(self, user_name: str, items=None):
        self.container = set()
        self.current_user = user_name
        if items:
            self.container.update(items)

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
            self.current_user: {
                "container": list(self.container)
            }
        }

        try:
            with open(filename, 'r') as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            existing_data = {}

        if self.current_user in existing_data:
            existing_data[self.current_user].update(data[self.current_user])
        else:
            existing_data.update(data)

        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)

    def load(self, filename = '/home/karas/studying/4-semester/SCoCS/02-lab/data.json'):
        with open(filename, "r") as f:
            data = json.load(f)

        for user, user_data in data.items():
            if user == self.current_user:
                loaded_container = user_data.get("container", [])
                self.container.update(loaded_container)
                return
        print("No such user")


    def switch(self, user):
        response = input("Do you want to save the container (y/n)")
        if response == "y":
            self.save()
        
        self.current_user = user
        self.container = set()
        try:
            with open('/home/karas/studying/4-semester/SCoCS/02-lab/data.json', 'r') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            print(f"Error: file  is empty or not valid JSON")
            return
    
        for cur_user, user_data in data.items():
            if cur_user == user:
                self.container = user_data.get("container", [])                

        print(f"Switched to user {user}")