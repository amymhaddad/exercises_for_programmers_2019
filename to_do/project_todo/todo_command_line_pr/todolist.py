"""Create a todo list with todos"""

from todo import ToDo

class ToDoList():
    """A model to create a todo list"""

    def __init__(self, list_name):
        self.list_name = list_name
        self.todos = []

    def add_todos(self, todo_name, due_date):
        """Add todos to the todo list"""

        if due_date:
            user_todo = ToDo(todo_name, due_date)
        else:
            user_todo = ToDo(todo_name)

        return self.todos.append(user_todo)

    def __repr__(self):
        return f"{self.list_name} {self.todos}"
