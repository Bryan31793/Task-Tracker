from task_operations import TaskOperations
import shlex

#command line interface
def cli():
    command = input()
    tokens = shlex.split(command) 

    if not tokens:
        return

    if tokens[0] != "task-cli":
        print(f"command {tokens[0]} not found")
        return   
    
    if len(tokens) < 2:
        print("Missing command")
        return 
    
    commands = {
        "add": handle_add,
        "update": handle_update,
        "delete": None,
        "mark": None,
        "list": None
    }
    
    cmd = tokens[1]
    handler = commands.get(cmd)

    if not handler:
        print(f"command {cmd} doesn't exist")
        return
    
    try:
        handler(tokens[2:])
    except Exception as e:
        print(e)

    

def handle_add(args: str) -> None:
    if len(args) != 1:
        raise ValueError("usage: task-cli add <description>")
    
    TaskOperations.add(args[0])

def handle_update(args: str) -> None:
    if len(args) != 2:
        raise ValueError("usage: task-cli update <id> <description>")
    
    try:
        args[0] = int(args[0])
    except ValueError:
        print("id must be an integer")
        
    TaskOperations.update(args[0], args[1])
    
cli()