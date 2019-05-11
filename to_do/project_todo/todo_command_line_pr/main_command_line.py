"""Get user data to create a todo list with todos"""

import sys
import csv
from todolist import ToDoList

def user_list_name():
    """Get user input on a todo list name"""

    return ToDoList(input("Enter a todo list name: "))

def get_todo_file(filename):
    """Get user todos from a file and return the todos"""

    try:
        with open(filename, newline='') as csvfile:
            user_todos = user_list_name()
            linereader = csv.reader(csvfile, delimiter=',')
            next(linereader)
            for row in linereader:
                todo_name, due_date = row[0], row[1]
                user_todos.add_todos(todo_name, due_date)
            print(user_todos.todos)

    except FileNotFoundError:
        print("File does not exist. Please try again.")

print(get_todo_file(sys.argv[1]))
