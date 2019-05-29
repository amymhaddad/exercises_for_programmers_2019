"""Get user input and create a todo list with todos"""

import sys
from todolist import ToDoList
from todo_list_file_management import (
    write_todo_list_json,
    read_todos_from_json,
    write_todos_to_csv,
    read_todos_csv_dict_reader,
    read_todos_csv_without_dict_reader,
)


def create_todo_list():
    """Get a todo list name from user"""
    print("Enter you todo list information when prompted. Type 'q' to quit.")
    list_name = input("Enter your todo list name: ")
    return ToDoList(list_name)


def add_todos_to_list():
    """Get todos and todo details from user"""
    user_todo_list = create_todo_list()

    while True:
        print("\n")
        todo = input("Enter a todo name: ")
        if todo == "q":
            break

        due_date = input("Enter a due date: ")
        status = input(
            "Enter the todo status. Or hit 'return' and the status will default to 'not started': "
        )

        user_todo_list.add_todos(todo, due_date, status)
    return user_todo_list


def update_todo_status(user_todos):
    """Get new todo status from user"""
    todo_name = input("What todo do you want to update? ")
    new_status = input("Enter your new todo status: ")

    return user_todos.update_status(todo_name, new_status)


def remove_todo(user_todos):
    """Get input from user on the todo to remove"""
    todo = input("What todo do you want to remove? ")

    return user_todos.remove_todo(todo)


user_todos = add_todos_to_list()

write_todo_list_json(sys.argv[1], user_todos)
read_todos_from_json(sys.argv[1])
write_todos_to_csv(sys.argv[1], user_todos)
read_todos_csv_dict_reader(sys.argv[1])
read_todos_csv_without_dict_reader(sys.argv[1])
