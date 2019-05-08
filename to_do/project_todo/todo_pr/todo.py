"""Create todos """

class ToDo():
    """Create a todo and add details to do, like due date and status"""

    def __init__(self, todo_name, due_date):
        self.todo_name = todo_name
        self.due_date = due_date

    def __repr__(self):
        return f"{self.todo_name} {self.due_date}"
