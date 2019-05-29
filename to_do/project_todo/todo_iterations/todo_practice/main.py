from todolist import ToDoList, ToDo
import sys
import csv

def user_todo_list():
    """Get a todo list name from user"""

    #create an instance with list_name that I can use in the ToDoList class
    user_list = input("Enter a todo list name: ")
    return ToDoList(user_list)


# with sys.argv: command line interface (ie, pip list, pip show, git rebase -i ---> giving git a command!)


def parse_todo_data(filename):
    try:
        new_todo_list = user_todo_list()
        with open(filename, newline='') as csvfile:
            linereader = csv.reader(csvfile, delimiter=',')
            next(linereader)
            for row in linereader:
                todo, due_date = row[0], row[1]
                new_todo_list.create_todos(todo, due_date)
            #why doesn't return work here --- I have to print?
            print(new_todo_list.todos)

    except FileNotFoundError:
        print("The file does not exist. Please try again.")

parse_todo_data(sys.argv[1])

















# def user_todo_list():
#     print("Enter todo list and information when prompted. Type 'q' to quit.\n ")
#     user_list = input("Enter a todo list name: ")
    
#     if user_list != 'q':
#         return ToDoList(user_list)


# def user_todo():
#     list = user_todo_list()

#     while True:
#         todo = input("Enter a todo name: ")
#         if todo == 'q':
#             return list
#             break
        
#         due_date = input("Enter a due date if known; otherwise hit return: ")
#         if due_date == 'q':
#             return list
#             break
        
#         else:
#             list.add_todo(todo, due_date)
            

# #Output:
# print(user_todo())

