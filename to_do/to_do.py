# class ToDoList():
#     def __init__(self):
#         # self.name = name
#         self.task = []

#     def add_task(self, name):
#         new_todo = ToDoDetails(name, due_date)
#         self.task.append(new_todo)

#     def __repr__(self):
#         return self.name

# todo1 = ToDoList()

# todo1.add_task('Exercise')
# todo1.add_task('Study')

# class ToDoDetails():
#     def __init__(self, name, due_date):
#         self.name = name
#         self.due_date = due_date
#         self.completed = False

#     def __str__(self):
#         return self.name 

# taska = ToDoDetails('run', 'feb 1')

# print(taska)


class ToDoList():
    def __init__(self, list_name):
        self.list_name = list_name
        self.tasks = []
    
    def add_task(self, todo_name, due_date):
        #passing in arg for class ToDo
        new_todo = ToDo(todo_name, due_date)
        self.tasks.append(new_todo)

class ToDo():
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

    def done(self):
        self.completed = True
    
    def __repr__(self):
        return self.name


todo_list_1 = ToDoList('Programming Task')

todo_list_1 = ToDoList('Programming Task')
todo_list_2 = ToDoList('Exercise Tasks')

todo_list_1.add_task('classes', 'apr 1')
todo_list_1.add_task('terminal', 'may 1')
todo_list_1.add_task('git', 'june 1')
print(todo_list_1.tasks)


first_todo_list = todo_list_1.tasks[0]
print(first_todo_list.name)
print(first_todo_list.due_date)

# first_todo_list.done()
# print(first_todo_list.completed)
