"""A template to create todos and todo details"""


class ToDo:
    """Create todos with details"""

    def __init__(self, todo_name, due_date, status="Not Complete"):
        self.todo_name = todo_name
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.todo_name}, {self.due_date}, {self.status}"
