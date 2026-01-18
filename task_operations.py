import json     #task are stored in json files
from pathlib import Path

#class containing all the actions you can realize
class TaskOperations():

    def __init__(self):
        pass

    #create a class
    def add(title: str, description: str) -> None:
        #dict that represents the task
        data = {
            "Title": title,
            "Description": description
            }
        
        file_path = Path('tasks.json')  #json file path 
        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)     #loads json file into memory
        else:
            tasks = []

        tasks.append(data)  #add the new task to the list
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)    #writes the list into the json file

    #update a task
    def update() -> None:
        pass

    #delete a task
    def delete() -> None:
        pass