#Why store the todos in a list?
#Why not add todos as an arg in __init__?

from todo import ToDo

class ToDoList():
    """List of todos"""

    #A todo list has a name AND todos
    def __init__(self, name):
        self.name = name
        self.todos = []

    def add_todo(self, todo_name, due_date):
        #Don't want to store the stuff inside self.todos as strings. I want to store it as a class so I can add a bunch of todo info
        self.todos = []

    def add_todo(self, todo_name, due_date):
        #Call ToDo class here and append an instance of the class to self.todos. 
        # I have a bunch of todo info to add and a class is the best data structure to hold a bunch of info -- not a string appended to a list

        #Deal with default here b/c that's the immediate caller of todo -- it's closest to the code.
        #Phrase is this way so it reads as a bool (if, true, then pass in the due date)
        if due_date:
            #This will override the default when truthy
            #call the class here b/c I'm creating a todo to add to the todo list. Pass in all args to ToDo.
            todo = ToDo(todo_name, due_date)

        elif due_date == '':
            #IF no due date is provided, then we rely on the default due_date and create an instance as such
            todo = ToDo(todo_name)
        #Regardless of whether or not there's a due_date passed in, I need to append the instance to the list of todos. 
        self.todos.append(todo)

    def __repr__(self):
        return f"{self.name} {self.todos}"
