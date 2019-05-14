import sys
from todolist import ToDoList

#Question: what if user enters multiple todos on command line? How to capture these? Need to specifiy a var for each todo entered on command line?
def get_todolist_name():
    list_name = input("Enter your todo list name: ")
    return ToDoList(list_name)

def get_todos():
    list = get_todolist_name()
    todo = sys.argv[1]
    due_date = sys.argv[2]
    
    list.add_todo(todo, due_date)
    print(list.todos)

get_todos()
