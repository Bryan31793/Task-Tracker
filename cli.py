from task_operations import TaskOperations
import shlex

#command line interface
def cli_input():
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
        "delete": handle_delete,
        "mark": handle_mark,
        "list": handle_list
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

    

def handle_add(args: list[str]) -> None:
    if len(args) != 1:
        raise ValueError("usage: task-cli add <description>")
    
    TaskOperations.add(args[0])

def handle_update(args: list[str]) -> None:
    if len(args) != 2:
        raise ValueError("usage: task-cli update <id> <description>")
    
    if not args[0].isdigit():
        raise ValueError("id must be integer")
    
    TaskOperations.update(int(args[0]), args[1])

def handle_delete(args: list[str]) -> None:
    if len(args) != 1:
        raise ValueError("usage: task-cli delete <id>")
    
    if not args[0].isdigit():
        raise ValueError("id must be integer")
    
    TaskOperations.delete(int(args[0]))

def handle_mark(args: list[str]) -> None:
    if len(args) != 2:
        raise ValueError("usage: task-cli mark <id> <status>")
    
    if not args[0].isdigit:
        raise ValueError("id must be integer")
    
    if args[1] != "done" and args[1] != "in-progress":
        raise ValueError("usage: status can be in-progress or done")

    TaskOperations.mark(int(args[0]), args[1]) 

def handle_list(args: list[str]) -> None:
    if len(args) == 0:
        TaskOperations.list_all()
        return
    
    if len(args) != 1:
        raise ValueError("usage: task-cli list  or   task-cli list <status>")
    
    if args[0] != "todo" and args[0] != "in-progress" and args[0] != "done":
        raise ValueError("usage: status can be todo, in-progress or done")
    
    TaskOperations.list_tasks(args[0])
    
    