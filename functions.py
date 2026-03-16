def get_todos(filepath = "files/todos.txt"):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath = "files/todos.txt"):
    with open(filepath,'w') as file:
            file.writelines(todos)