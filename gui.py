import functions
import FreeSimpleGUI as sg
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w"):
        pass

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45 ,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("Todo list", 
                layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window["todos"].update(value=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_value = values["todo"]
                functions.write_todos(todos)
                window["todos"].update(value=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(value=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED | "Exit":
            break

window.close()