todos = []

while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    
    match user_action:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo.title())
        case "show":
            print(todos)
        case "edit":
            number = input("Number todo to edit: ")
            if(number > len(todos)):
                print("There is no such todo in the list")
                break
            
            index = int(number) - 1;
            
            if(index < 0):
                print("list is empty")
                break
            todos[index] = input("Enter new value: ")
        case "exit":
            break
        case _:
            print("Incorrect command")