

class ToDoList():
    """Create a todo list"""

    def __init__(self, list_name):
        self.list_name = list_name
        self.todo_dict = {}


    def create_todos(self, todo_name, due_date, status):
        self.todo_dict[todo_name] = [due_date, status]
    
    
    def remove_todo(self, todo_name):
        del self.todo_dict[todo_name]
     

    def update_status(self, todo_name, new_status):
        for todo, todo_item in self.todo_dict.items():
            if todo == todo_name:
                todo_item[1] = new_status       
    

    def __repr__(self):
        return f"{self.list_name} {self.todo_dict}"


class ToDo():
    """Add details to each todo"""

    def __init__(self, todo_name, due_date, status):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.due_date} {self.status}"


# list1 = ToDoList('work')
# list1.create_todos('read', 'may1', 'not started')
# list1.create_todos('program', 'may1', 'not started')
# list1.create_todos('study', 'june1', 'not started')
# list1.update_status('read', 'complete')

# print(list1.todo_dict)

