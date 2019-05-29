from todolist import ToDoList, ToDo
import csv
import sys
import json

def get_list_name():
    print("Enter you todo list information when prompted. Type 'q' to quit.")
    list_name = input("Enter your todo list name: ")
    return ToDoList(list_name)

def get_user_todos():
    user_todo_list = get_list_name()

    while True:
        print('\n')
        todo = input("Enter a todo name: ")
        if todo == 'q':
            break
        
        due_date = input("Enter a due date: ")
        if due_date == 'q':
            break
        
        status = input("Enter the todo status, otherwise hit return and the status will default to \'not started\': ")
        if status == 'q':
            break
        
        else:
            user_todo_list.add_todos(todo, due_date, status)
    
    #this holds all the stuff in the todo, when an attribute is called on it. Right now I just return the instance
    return user_todo_list

#use a variable to keep a reference to the instance. x is an instance 
# x = get_user_todos()
# It's always best to return the instance so i have control. Otherwise, if I return an instance that calls a attribute (ie, user_todo_list.dict_todos) you have much less flexibility. 
# You lose your variable refernce to that instance. Once the function completes, it is lost.


def write_todos_to_json(filename):
    #call get_user_todos() to create an instance. Then I can call attributes on this instance to create a json object.
    todo_list = get_user_todos()

    json_dict = {
        'list name' : todo_list.list_name,
        'todos' : todo_list.todo_details,
    }
    
    import pdb; pdb.set_trace()


write_todos_to_json(sys.argv[1])


# 1. Create a dictionary that has the same shape as the one below. You already have the first key done.

# write_todos_to_json('user_todos.json')

# # {
# #     label_called_name: 'todolist name',
# #     lable_called_todos: [
            # <List the todos in a list>
# #         <Todo ...>,
# #         <Todo ...>,
# #         <Todo ...>,
# #     ]
# # }

# {'list name': 'wokr', 'todos': [a a a, b b b]}


# { 
#     'name': 'work'
#     'todos': ['todo1 may 1 started', 'todo2 may 15 complete']
# }

#2. Once the dictionary matches the above, practice calling json.dumps, passing in this dictionary, to get a JSON object. It should have a similar structure as your dictionary with some extra quotes.

#Stop using print and instead use pdb frequently when debugging to test my expectations