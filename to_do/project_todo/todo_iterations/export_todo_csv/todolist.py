
class ToDoList():

    def __init__(self, list_name):
        self.list_name = list_name
        self.todos = []

    def add_todo(self, todo, due_date):
        if due_date:
            user_todo = ToDo(todo, due_date)
        elif due_date == '': 
            user_todo = ToDo(todo)
        self.todos.append(user_todo)

    def __repr__(self):
        return f"{self.list_name} {self.todos}"


class ToDo():

    def __init__(self, todo, due_date='TBD'):
        self.todo = todo
        self.due_date = due_date

    def __repr__(self):
        return f"{self.todo}: {self.due_date}"



# list1 = ToDoList('work')
# list1.add_todo('program')

# print(list1.todos)
