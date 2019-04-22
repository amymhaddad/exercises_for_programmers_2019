
"""Class to create a todo list with individual todo's"""

class ToDoList():
    """Create a todo list"""
    def __init__(self, list_name):
        self.list_name = list_name
        self.tasks = []
    
    def add_task(self, todo_name, due_date):
        """Update task with task details"""
        new_task = ToDoDetails(todo_name, due_date)
        self.tasks.append(new_task)

    def __repr__(self):
        return self.tasks

class ToDoDetails():
    """Create individual todo's for each task list"""
    def __init__(self, todo_name, due_date):
        self.todo_name = todo_name
        self.due_date = due_date
        self.completed = False

    def done(self):
        self.completed = True

list1 = ToDoList("Programming")
list1.add_task("learn classes", "May 1")
list1.add_task("write tests", "June 1")

task_details1 = list1.tasks[0]
print(task_details1.todo_name)
print(task_details1.due_date)

task_details1.done()
print(task_details1.completed)