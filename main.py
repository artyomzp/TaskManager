while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    
    match user_action:
        case "add":
            todo = input("Enter todo: ") + "\n"

            with open('files/todos.txt','r') as file:
                todos = file.readlines()
            
            todos.append(todo.title())

            with open('files/todos.txt','w') as file:
                file.writelines(todos)

        case "show":
            with ('files/todos.txt','r') as file:
                todos = file.readlines()

            cleaned_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(cleaned_todos):
                string = f"{index + 1}-{item}"
                print(string)

        case "edit":
            with open('files/todos.txt','r'):
                todos = file.readlines()
            
            number = input("Number todo to edit: ")
            if(number > len(todos)):
                print("There is no such todo in the list")
                break
            
            index = int(number) - 1;
            
            if(index < 0):
                print("list is empty")
                break
            todos[index] = input("Enter new value: ")
        case "complete":
            number = input("Number todo to complete: ")

            with open('files/todos.txt','r') as file:
                todos = file.readlines()
            
            todo_to_remove = todos[number -1]

            todos.pop(number -1)

            with open('files/todos.txt','w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from todo list."

        case "exit":
            break
        case _:
            print("Incorrect command")