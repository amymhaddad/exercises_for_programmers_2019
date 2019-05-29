from v2_todolist import ToDoList, ToDo
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
    return user_todo_list

def write_todos_to_json(filename):
    #call get_user_todos() to create an instance. Then I can call attributes on this instance to create a json object.
    todo_list = get_user_todos()
    #todo_details is an instance, but everything in json has to be string, list, dict, etc. If not, must convert for json to work
    todos  = [str(todo_details) for todo, todo_details in todo_list.dict_todo.items()]

    
    json_dict = {
        'list name' : todo_list.list_name,
        'todos' : todos,
    }           
    with open(filename, 'w') as f_object:
    #Use json.dump and pass the user_input and f_object to sreo int a file
        json.dump(json_dict, f_object)


write_todos_to_json(sys.argv[1])
#json.dumps() writes converts the dict to json but doesn't write it to a file. this why i can see it in the console. use for testing
#T  o write to a file, use json.dump()


def read_todos_from_json(filename):

    with open(filename) as f_object:
        todos = json.load(f_object)
        import pdb; pdb.set_trace()
    return todos

read_todos_from_json(sys.argv[1])



def write_todos_to_csv(filename):
    user_todos = get_user_todos()
    todos = [str(todo_details) for todo, todo_details in user_todos.dict_todo.items()]


    #what if I want to separate out each part of todo (ie, due_date, status, etc). I can't seem to iterate through todos to grab each element

    dict_csv = {
        'list name': user_todos.list_name,
        'todos': todos
    }
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['list name', 'todos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(dict_csv)


write_todos_to_csv(sys.argv[1])


# def read_csv_info(file):

#     todos = []
#     with open(file, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         #using next to skip the header, but get error
#         next(reader)
#         for row in reader:
#             todos.append(row)
#         # import pdb; pdb.set_trace()
# read_csv_info('user_todos.csv')