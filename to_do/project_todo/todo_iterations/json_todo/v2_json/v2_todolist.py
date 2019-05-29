

class ToDoList():

    def __init__(self, list_name):
        self.list_name = list_name
        self.dict_todo = {}
    
        # self.list_todos = self.dict_todo.values()

    def add_todos(self, todo_name, due_date, status):
        if status:
            user_todo = ToDo(todo_name, due_date, status)
        elif status == '':
            user_todo = ToDo(todo_name, due_date)
        self.dict_todo[todo_name] = user_todo

    def update_status(self, todo_name, new_status):
        #todo gets ONLY the todos. Then I can grab the status attribute and update it.
        todo = self.dict_todo[todo_name] 
        todo.status = new_status

    def remove_todo(self, todo):
        del self.dict_todo[todo]

    def __repr__(self):
        return f"{self.list_name} {self.dict_todo}"
    
class ToDo():

    def __init__(self, todo_name, due_date, status='Not complete'):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = status
    
    def __repr__(self):
        return f"{self.todo_name}, {self.due_date}, {self.status}"


# list1 = ToDoList('work')
# list1.add_todo('program', 'may 1', 'complete')
# list1.add_todo('read', 'may 1', 'complete')
# list1.remove_todo('program')
# print(list1.dict_todo)


