
class ToDoList():

    
    def __init__(self, list_name):
        self.list_name = list_name
        self.todos_dict = {}

#I don't pass in status b/c it's a default and will be automatically added to the instance, as long as I CALL the instance.
#IF user provides a status, call update status method?
    def add_todos(self, todo, due_date, status):

        if status:
            user_todo = ToDo(todo, due_date, status)
        elif status == "":
            user_todo = ToDo(todo, due_date)
        
        self.todos_dict[self.todo] = user_todo
    

    def update_status(self, todo, new_status):
        #Index into the dictionary using the id. This gets all of the "todo info" associated with a specific todo_list
        #This will give me ALL of the todo details associated with this one todo list
        user_todo = self.todos_dict[todo]

        #Now I can just get the todo I want to update
        user_todo.status = 'complete'
        

    def remove_todo(self, list_id):
        del self.todos_dict[list_id]


    def __repr__(self):
        return f"{self.list_name} {self.todos_dict}"
    
class ToDo():

    def __init__(self, todo, due_date, status='Not Started'):
        self.todo = todo
        self.due_date = due_date
        self.status = status

    def __repr__(self):
        return f"{self.todo}, {self.due_date}, {self.status}"


# list1 = ToDoList('work')
# list1.add_todos("program", "may 1")

# list2 = ToDoList('vacation')
# list2.add_todos("research", "may 17")

# list2.update_status(2, 'started')

# # list2.remove_todo(2)

# print(ToDoList.todo_dict)
