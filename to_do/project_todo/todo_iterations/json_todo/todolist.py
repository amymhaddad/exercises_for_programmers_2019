
class ToDoList():
    #can't make the dictionary a class var bc each todolist is separate. The dont' need to be combined --- ie, list1 won't need list2

    def __init__(self, list_name):
        self.list_name = list_name
        # get dict_todos working, but recommmend changing its name to todos
        self.dict_todos = {}
        # self.todo_details = []
    
    def add_todos(self, todo_name, due_date, status):
        if status:
            user_todo = ToDo(todo_name, due_date, status)
        elif status == '':
            user_todo = ToDo(todo_name, due_date)
        
        #In order to add unique todos to the dictionary, I need to index with todo_name -- not self.list_name. 
        # self.list_name will always be the most recent name entered. It'll override what was there before
        #what dict should look like:
        # key(todo_name): value(ToDo instance)
        self.todo_details.append(user_todo)
        self.dict_todos[todo_name] = user_todo

        # {
        #     "my_first_todo": <Todo ...>,
        #     "my_second_todo": <Todo ...>,
        # }

        # {
        #     "list_name": <Todo ...>
        # }
 

    def update_status(self, todo_name, new_status):

        #index into the dictionary and get all of the todos for one specific todo list
        #This is jsut the template, so I don't need to update todo_name with the ToDo class (this will be taken care of by the user of the class, in this case main.py )
        todo = self.dict_todos[todo_name]
        todo.status = new_status
        
    def __repr__(self):
        return f"{self.list_name} {self.dict_todos}"


class ToDo():

    def __init__(self, todo_name, due_date, status="Not Completed"):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = status

        #If i had: self.stat = "Not complete" and add status to the paramter, then "not complete" will ALWAYS default to "not complete". The way it's set up right now, I can override the default status.

    def __repr__(self):
        return f"{self.todo_name} {self.due_date} {self.status}"

# #each instance will need multiple todos 
# t = ToDoList('work')
# t1 = ToDoList('play')