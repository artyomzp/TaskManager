from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    user_action.strip()
    
    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:]

        todos = get_todos()
        
        todos.append(todo.title())

        write_todos(todos)

    elif user_action.startswith("show") :
        
        todos = get_todos()

        cleaned_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(cleaned_todos):
            string = f"{index + 1}-{item}"
            print(string)

    elif user_action.startswith("edit"):
        try:
            number = user_action[5:]       
            
            todos = get_todos()
            
            if(number > len(todos)):
                print("There is no such todo in the list")
                break
            
            index = int(number) - 1;
            
            if(index < 0):
                print("list is empty")
                break
            todos[index] = input("Enter new value: ")
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            
            todo_to_remove = todos[number -1]

            todos.pop(number -1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from todo list."
            print(message)
        except IndexError:
            print("There is no task with such number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")