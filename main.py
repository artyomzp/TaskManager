while True:
    user_action = input("Type add, show, edit or exit: ").strip()
    
    match user_action:
        case "add":
            todo = input("Enter todo: ") + "\n"

            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()

            todos.append(todo.title())

            file = open('files/todos.txt','w')
            file.writelines(todos)
            file.close()

        case "show":
            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()

            cleaned_todos = [item.strip("\n") for item in todos]

            for index, item in enumerate(cleaned_todos):
                string = f"{index + 1}-{item}"
                print(string)

        case "edit":
            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()
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
            todos.pop(number -1)
        case "exit":
            break
        case _:
            print("Incorrect command")