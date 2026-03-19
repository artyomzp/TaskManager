import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Todo list", 
                layout=[[label], [input_box, add_button]],
                font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "add" :
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
        case sg.WIN_CLOSED:
            break

window.close()