
import csv
import sys
from todolist import ToDoList

def get_listname():
    print("Enter todo information when prompted. Type 'q' to quit.")
    list_name = input("Enter a todo list name: ")
    return ToDoList(list_name)


def add_todos_to_list():
    list_name = get_listname()

    while True:
        print('\n')
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
            list_name.create_todos(todo, due_date, status)
    return list_name.todo_dict


#Write a dictionary to a csv


# def list_of_todos():

#     list_todos = get_user_todo()
#     return [[todo] for todo in list_todos.todos]


# def write_to_csv(filename, todos):

#     with open(filename, mode='w') as csvfile:
#         linewriter = csv.writer(csvfile)
#         linewriter.writerows(todos)

# write_to_csv(sys.argv[1], list_of_todos())
