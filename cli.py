from task_operations import TaskOperations

#command line interface
def cli():
    command = input()
    command_list = command.split()

    if command_list[0] == "task-cli":
        if len(command_list) == 1:
            raise ValueError("Missing command")
        if command_list[1] == "add":
            if len(command_list) == 2:
                raise ValueError("Missing argument")
            if len(command_list) > 3:
                raise ValueError(f"{command_list[3]} not found")
            
            TaskOperations.add(command_list[2])
        elif command_list[1] == "update":
            if len(command_list) < 4:
                raise ValueError("Missing argument")
            if len(command_list) > 4:
                raise ValueError(f"{command_list[4]} not found")
            try:
                TaskOperations.update(command_list[2], command_list[3])
            except FileNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
            except KeyError as e:
                print(e)
    else:
        raise ValueError(f"{command_list[0]} not found")
    
