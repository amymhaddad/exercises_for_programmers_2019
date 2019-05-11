"""Create todos and add details to them"""

class ToDo:
    """A model to create todos"""

    def __init__(self, todo_name, due_date='TBD'):
        self.todo_name = todo_name
        self.due_date = due_date

    def __repr__(self):
        return f"{self.todo_name}: {self.due_date}"
