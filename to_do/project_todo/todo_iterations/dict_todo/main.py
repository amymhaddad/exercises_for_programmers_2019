
import csv
import sys
from todolist import ToDoList

def get_listname():
    print("Enter todo information when prompted. Type 'q' to quit.")
    list_name = input("Enter a todo list name: ")
    return ToDoList(list_name)


def add_todos_to_list():
    list_name = get_listname()

    todo_id = 0

    while True:
        print('\n')
        todo_id += 1
        todo = input("Enter a todo name: ")
        if todo == 'q':
            break
        
        due_date = input("Enter a due date: ")
        if due_date == 'q':
            break
        
        status = input("Enter the todo status: ")
        if status == 'q':
            break
        
        else:
            list_name.create_todos(todo, due_date, status, todo_id)

    return list_name.todo_dict


def write_to_csv(filename):
    todos_dict = add_todos_to_list() 

    with open(filename, 'w') as csvfile:
        fieldnames = ['Todo Name', 'Due Date', 'Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        user_details = [dict(zip(fieldnames, todo_details)) for todo, todo_details in todos_dict.items()]
        writer.writerows(user_details)
   
write_to_csv(sys.argv[1])
