#Question1:  how to make a header and write mutliple things from multiple functions to a csv


import csv
import sys
from todolist import ToDoList

def get_listname():
    print("Enter todo information when prompted. Type 'q' to quit. \n")
    list = input("Enter a todo list name: ")
    return ToDoList(list)


def add_todos_to_list():
    list = get_listname()

    while True:
        todo = input("Enter a todo name: ")
        if todo == 'q':
            return list
            break
        
        due_date = input("Enter a due date if known; otherwise hit return: ")
        if due_date == 'q':
            return list
            break
        
        else:
            list.create_todos(todo, due_date)
    return list


#This isn't working. Trying to convert the user todo list name to a string and append everything -- including todos and date -- to a new list
def put_user_todos_into_list():
    list = []
    name = str(get_listname())
    header = [name, 'ToDo ' , ' DueDate']
    
    for item in header:
        list.append(header)

    for todos in add_todos_to_list().todos:
        list.append(todos)

    return list


print(put_user_todos_into_list())


#Correct way to write multi things from multi functions to csv?
def write_to_csv(filename, list_name, todos):
    with open(filename, mode='w') as csvfile:
        linewriter = csv.writer(csvfile)
        linewriter.writerow(['List name', 'To Do' , 'Due Date' ])

    # with open(filename, mode='a') as csvfile:
    #     linewriter = csv.writer(csvfile)
    #     linewriter.writerow([list_name])

    with open(filename, mode='a') as csvfile:
        linewriter = csv.writer(csvfile)
        linewriter.writerows([list_name], todos)

write_to_csv(filename=sys.argv[1], list_name=get_listname(), todos=put_user_todos_into_list())

