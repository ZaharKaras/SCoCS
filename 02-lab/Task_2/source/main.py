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
    
    for user, user_data in data.items():
        if user == username:
            response = input("Do you want to download the contents of the container (y/n): ")
            if response == "n":
                return SetContainer(username)
            
            container_data = user_data.get("container", [])
            container = SetContainer(username ,container_data)
            return container

    return None


if __name__ == "__main__":
    

    user = input("Enter username: ")
    container = find_container_by_username(user)
    #container = SetContainer(user)
    if container is None:
        print(f"No container found for user '{user}'. Creating new container.")
        container = SetContainer(user)

    controller = Controller(container)
    cli = CLI(controller, user)

    cli.run()