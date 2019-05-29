list
#From video call
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




Step1: start with most simple thing and what I want to see: a todo list with a name
#todo_list_1 = ToDoList('Programming Task')
#Run program, see error and write the correct code

todo_list_1 = ToDoList('Programming Task')
print(todo_list_1.list_name)

todo_list_2 = ToDoList('Exercise Tasks')


#Step2: each todo has tasks, so I need to add tasks. So I type out what I want and run the program and see what happens
# print(todo_list_1.tasks)

#Step3: I want to add a single item to the task list with certain characteristics. Note that this is a behavior
#I don't want to call the instance.task to add a task b/c that's hardcoding and it won't persist
todo_list_1.add_task('classes')
todo_list_1.add_task('terminal')
todo_list_1.add_task('git')
print(todo_list_1.tasks)

#Step 4: I want to add more detail to a task, other than the name. So I grab the first task in the todo list
first_todo_list = todo_list_1.tasks[0]

#Step5: type out what I want: a name for a todo. I need an object that will hold lots of info on an indiv todo: name, duedate, status. So I need to create a class
print(first_todo_list.name)

first_todo_list = todo_list_1.tasks[0]
print(first_todo_list.name)
print(first_todo_list.due_date)

#side effect method --> call it but it doesn't return anything. It updates the state
first_todo_list.done()
print(first_todo_list.completed)
