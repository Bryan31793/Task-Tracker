import json     #task are stored in json files
from pathlib import Path
from datetime import datetime

#class containing all the actions you can realize
class TaskOperations():

    def __init__(self):
        pass

    #create a task
    def add(self, description: str) -> None:

        file_path = Path('id_file.txt')
        if file_path.exists():
            with open('id_file.txt', 'r') as file:
                id_task = int(file.read())

            with open('id_file.txt', 'w') as file:
                file.write(str(id_task + 1))
        else:
            id_task = 0
            with open('id_file.txt', 'w') as file:
                file.write('1')
        #dict that represents the task
        now = datetime.now()
        data = {
            "id": id_task,
            "description": description,
            "status": "todo",
            "createdAt": str(now),
            "updatedAt": None
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
    def update(self, id_task: int, new_description: str = None) -> None:
        
        file_path = Path('tasks.json')

        if not file_path.exists():
            raise FileNotFoundError("file tasks.json doesn't exist")
        
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)

        for t in tasks:
            if t['id'] == id_task:
                if not new_description:
                    raise ValueError("new description can't be empty")
                
                t['description'] = new_description
                t["updatedAt"] = str(datetime.now())

                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file, indent=4)

                return

        raise KeyError(f"id {id_task} doesn't exist")
        

    #delete a task
    def delete(self, id_task: int) -> None:
        file_path = Path('tasks.json')

        if not file_path.exists():
            raise FileNotFoundError("file tasks.json doesn't exist")
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file) 
        
        new_tasks = []
        for t in tasks:
            if t['id'] != id_task:
                new_tasks.append(t)

        if len(new_tasks) == len(tasks):
            raise KeyError(f"id {id_task} doesn't exist")
        
        with open('tasks.json', 'w') as file:
            json.dump(new_tasks, file, indent=4)

    #mark task as in progress or done
    def mark(self, id_task: int, status: str) -> None:
        file_path = Path('tasks.json')

        if not file_path.exists():
            raise FileNotFoundError("file tasks.json doesn't exist")
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        
        for t in tasks:
            if tasks["id"] == id_task:
                tasks["status"] = status
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file, indent=4)        
                
                return
            
        raise KeyError(f"id {id_task} doesn't exist")

    #list all tasks
    def list_all(self):
        file_path = Path('tasks.json')

        if not file_path.exists():
            raise FileNotFoundError("file tasks.json doesn't exist")

        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        for t in tasks:
            print(f"id: {t["id"]}")
            print(f"description: {t["description"]}")
            print(f"status: {t["status"]}")

    #list all tasks that are not done, done and in progress
    def list_tasks(self, status: str = None):
        file_path = Path('tasks.json')

        if not file_path.exists():
            raise FileNotFoundError("file tasks.json doesn't exist")
        
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        
        for t in tasks:
            if status == t["status"]:
                print(f"id: {t["id"]}")
                print(f"description: {t["description"]}")
                print(f"status: {t["status"]}")

obj = TaskOperations()

#obj.add("buy groceries")
obj.update(0, "new task")