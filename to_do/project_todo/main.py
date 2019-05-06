
#QUETIONS:
#Why not include self.todos as an arg in todolist? Is it b/c this prob asks to get user input?

from todo import ToDo
from todolist import ToDoList 

#this todolist contains only one list so I don't need a container vs cityreader has multiple city instances so I need a list as a container to store them all
def create_todo_list():
    """Get name of todo list from user"""

    list_name = input("Enter a todo list name: ")
    #creating a new instance of ToDoList and passing in list_name (which contains the user's input) as the arg
    return ToDoList(list_name)


def user_todos():
    """Get todos from user"""

    print("Enter your todo information when prompted. Type 'q' to quit.\n")
    #Take the info from create_todo_list (bc that work is already done) and use it in this function. 
    #The function above returns an instance of the class. This function (user_todos) adds to that function by calling the add_todo method from the class, and passing user info to that class.
    user_todo_list = create_todo_list()

    while True:
        todo = input("Enter your todo: ")
        if todo == 'q':
            return user_todo_list
            break

        due_date = input("Enter due date if it's known, otherwise hit return: ")

        if due_date == 'q':
            return user_todo_list
            break
        else:
            #user_todo_list is an instance and I'm calling add_todo method on this instance, passing in todo (which contains the users input) and due_date (I deal with due_date info in the class itself)
            user_todo_list.add_todo(todo, due_date)
            

#This is the output
todo_list = user_todos()
print(todo_list)

