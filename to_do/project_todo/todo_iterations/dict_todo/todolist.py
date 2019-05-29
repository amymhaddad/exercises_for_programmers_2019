

class ToDoList():
    """Create a todo list"""
    #create a class var with an id; remove id from main.py

    def __init__(self, list_name):
        self.list_name = list_name
        self.todo_dict = {}


    def create_todos(self, todo_name, due_date, status, todo_id):
        new_todo = ToDo(todo_name, due_date, status)
        self.todo_dict[todo_id] = [new_todo]
    
    
    def remove_todo(self, todo_id):
        del self.todo_dict[todo_id]
     

    #recall create_todo with new status
    #Use the id that I'm passing in to look up the dicitionary  value
    def update_status(self, id, status):
        updated_todo = ToDo(todo_name, due_date, status, todo_id)
        self.create_todos(updated_todo)
    
 
    def __repr__(self):
        return f"{self.list_name} {self.todo_dict}: "


class ToDo():
    """Add details to each todo"""

    def __init__(self, todo_name, due_date, status):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.todo_name}, {self.due_date}, {self.status}"


list1 = ToDoList('work')
list1.create_todos('read', 'may1', 'not started', 1)
# list1.create_todos('program', 'may1', 'not started', 2)
# list1.create_todos('study', 'june1', 'complete')
list1.update_status(1, "completed")

print(list1.todo_dict)

