"""A template to create a todo list with todos"""
from todo import ToDo


class ToDoList:
    """Create a todo list and add todos to it"""

    def __init__(self, list_name):
        self.list_name = list_name
        self.all_todos = {}

    def add_todos(self, todo_name, due_date, status):
        """Add todos to the todo collection"""

        user_todo = ToDo(todo_name, due_date, status)
        self.all_todos[todo_name] = user_todo

    def update_status(self, todo_name, new_status):
        """Update the status of the todo"""

        todo = self.all_todos[todo_name]
        todo.status = new_status

    def remove_todo(self, todo_name):
        """Remove a todo"""

        del self.all_todos[todo_name]

    def __repr__(self):
        return f"{self.list_name} {self.all_todos}"
