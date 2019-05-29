
class ToDoList():
    

    def __init__(self, list_name):
        self.list_name = list_name
        self.dict_todos = {}
    
    def add_todos(self, todo_name, due_date, status):
        if status:
            user_todo = ToDo(todo_name, due_date, status)
        else:
            user_todo = ToDo(todo_name, due_date)
        
        self.dict_todos[self.list_name] = user_todo

    def update_status(self, new_status):
        #index into the dictionary and get all of the todos for one specific todo list
        todo = Tself.dict_todos[self.list_name]
        todo.status = new_status
        
    def __repr__(self):
        return f"{self.list_name}"


class ToDo():

    def __init__(self, todo_name, due_date, status):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = "Not complete"

    def __repr__(self):
        return f"{self.todo_name} {self.due_date} {self.status}"
