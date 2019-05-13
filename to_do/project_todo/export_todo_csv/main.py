"""Create a todo list and export information to a csv file"""

from todolist import ToDoList
import csv
FILENAME = 'user_todo_info.csv'

def get_user_todolist():
    """Get name of todo list from user"""

    print("Enter todo information when prompted. Type q to quit.\n")
    list = input("Enter the name of your todo list: ")
    return ToDoList(list)

def add_user_todos_to_todolist():
    """Add todos and todo information to the todo list"""

    user_list = get_user_todolist()
    while True:
        todo = input("Enter a todo: ")
        if todo == 'q':
            return user_list
            break

        due_date = input("Enter the due date if know. Otherwise hit return: ")
        if due_date == 'q':
            return user_list
            break
        user_list.add_todo(todo, due_date)

user_todolist_with_todos = add_user_todos_to_todolist()


def get_user_todos(user_todolist_with_todos):
    """Put all the todo information into a list"""

    todo_list = [[user_todolist_with_todos.list_name]]

    for todo in user_todolist_with_todos.todos:
        todo_list.append([todo])
    return todo_list

list_of_todos = get_user_todos(user_todolist_with_todos)


def export_todos_csv(FILENAME, list_of_todos):
    """Write todo list information to a csvfile"""

    with open(FILENAME, mode='w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list_of_todos)
    csvfile.close()

export_todos_csv(FILENAME, list_of_todos)
