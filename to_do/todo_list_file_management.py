"""Practice using several ways to read and write user todos to a file"""
import json
import csv


def write_todo_list_json(filename, user_todos):
    """Write user todos to a json file"""
    todos = [str(todo_details) for todo, todo_details in user_todos.all_todos.items()]

    user_todos = {"list name": user_todos.list_name, "todos": todos}

    with open(filename, "w") as file:
        json.dump(user_todos, file)


def read_todos_from_json(filename):
    """Read in todos from json file"""
    with open(filename) as file:
        return json.load(file)


def write_todos_to_csv(filename, user_todos):
    """Write user todos to a csv file"""
    with open(filename, mode="w", newline="") as csvfile:
        fieldnames = ["todo name", "due date", "status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for name, todo in user_todos.all_todos.items():
            name = todo.todo_name
            due_date = todo.due_date
            status = todo.status

            writer.writerow({"todo name": name, "due date": due_date, "status": status})


def read_todos_csv_dict_reader(filename):
    """Read todos from a csv file with an ordered dict"""
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row["todo name"], row["due date"], row["status"])


def read_todos_csv_without_dict_reader(filename):
    """Read todos from a csv file without an ordered dict"""
    todos = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            todos.append(row)
    print(todos)
