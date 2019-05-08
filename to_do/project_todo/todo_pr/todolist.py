"""Use input from user to create a todo list"""

from todo import ToDo

class ToDoList():
    """A list of todos"""

    def __init__(self, list_name):
        self.list_name = list_name
        self.todos = []

    def add_todo(self, todo, due_date):
        """Add each todo instance to a list of todos"""

        user_todo = ToDo(todo, due_date)
        self.todos.append(user_todo)

    def __repr__(self):
        return f"{self.list_name} {self.todos}"
