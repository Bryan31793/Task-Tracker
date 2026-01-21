import json     #task are stored in json files
from pathlib import Path

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
        data = {
            "id": id_task,
            "description": description,
            "status": "todo"
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
    def update(self, id_task: int, new_description: str) -> None:
        
        file_path = Path('tasks.json')

        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
            for t in tasks:
                if t['id'] == id_task:
                    if new_description:
                        t['description'] = new_description

                    with open('tasks.json', 'w') as file:
                        json.dump(tasks, file, indent=4)

                    return
        else:
            print("Exeption")   #usar excepcion

    #delete a task
    def delete(self, id_task: int) -> None:
        file_path = Path('tasks.json')

        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file) 
            
            new_tasks = []
            for t in tasks:
                if t['id'] != id_task:
                    new_tasks.append(t)

            with open('tasks.json', 'w') as file:
                json.dump(new_tasks, file, indent=4)
        else:
            print("Exeption")   #usar excepcion

    #mark task as in progress or done
    def mark(self, id_task: int, status: str) -> None:
        file_path = Path('tasks.json')

        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
            
            i = 0
            while(tasks[i]["id"] != id_task and i < len(tasks)):
                i += 1
            if i < len(tasks):
                tasks[i]["status"] = status

            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
        else:
            print("Exeption")   #usar excepcion

    #list all tasks
    def list_all(self):
        file_path = Path('tasks.json')

        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
            for t in tasks:
                print(f"id: {t["id"]}")
                print(f"description: {t["description"]}")
                print(f"status: {t["status"]}")

    #list all tasks that are not done, done and in progress
    def list_tasks(self, status: str = None):
        file_path = Path('tasks.json')

        if file_path.exists():
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
            
            for t in tasks:
                if status == t["status"]:
                    print(f"id: {t["id"]}")
                    print(f"description: {t["description"]}")
                    print(f"status: {t["status"]}")
        else:
            print("Exeption")   #usar excepcion
