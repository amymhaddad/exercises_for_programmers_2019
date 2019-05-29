from todolist import ToDoList
import sys

#Option 1: using sys.argv to get user input FROM command line and return todos and due date.
#Question: what if user enters multiple todos on command line? How to capture these? Need to specifiy a var for each todo entered on command line?
def get_todolist_name():
    list_name = input("Enter your todo list name: ")
    return ToDoList(list_name)

def get_todos():
    list = get_todolist_name()
    todo = sys.argv[1]
    due_date = sys.argv[2]
    
    list.create_todos(todo, due_date)
    print(list.todos)

get_todos()

#Option 2: using sys.argv -- user enters the filename on the command line
def get_todolist_name():
    list_name = input("Enter your todolist name: ")
    return ToDoList(list_name)

def user_todos(todo_file):
    list = get_todolist_name()

    try:
        with open(todo_file, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            next(linereader)
            for row in linereader:
                todo, due_date = row[0], row[1]
            list.create_todos(todo, due_date)
            return list.todos
    except FileNotFoundError:
        print("This file doesn't exist. Please try again.")

user_todos(sys.argv[1])
