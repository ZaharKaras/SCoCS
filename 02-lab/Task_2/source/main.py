from cli import CLI
from controller import Controller
from container import SetContainer

import json

def find_container_by_username(username):
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        print(f"Error: file  is empty or not valid JSON")
        return None
    
    for container in data["container"]:
        if container['current_user'] == username:
            return container
    
    return None


if __name__ == "__main__":
    

    user = input("Enter username: ")
    container = find_container_by_username(user)
    if container is None:
        print(f"No container found for user '{user}'. Creating new container.")
        container = SetContainer(user)

    controller = Controller(container)
    cli = CLI(controller, user)

    cli.run()