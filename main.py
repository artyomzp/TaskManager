while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    print('add' in user_action)
    
    if "add" in user_action or "new" in user_action:
        todo = user_action[4:]

        with open('files/todos.txt','r') as file:
            todos = file.readlines()
        
        todos.append(todo.title())

        with open('files/todos.txt','w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open('files/todos.txt','r') as file:
            todos = file.readlines()

        cleaned_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(cleaned_todos):
            string = f"{index + 1}-{item}"
            print(string)

    elif "edit" in user_action:
        number = user_action[5:]       
        with open('files/todos.txt','r'):
            todos = file.readlines()
        
        if(number > len(todos)):
            print("There is no such todo in the list")
            break
        
        index = int(number) - 1;
        
        if(index < 0):
            print("list is empty")
            break
        todos[index] = input("Enter new value: ")

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt','r') as file:
            todos = file.readlines()
        
        todo_to_remove = todos[number -1]

        todos.pop(number -1)

        with open('files/todos.txt','w') as file:
            todos = file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from todo list."
        print(message)

    elif "exit" in user_action:
        break
    else:
        print("Command is not valid")