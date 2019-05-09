
class ToDo():
    """Details for each todo"""

    def __init__(self, name, due_date='TBD'):
        self.name = name
        self.due_date = due_date
        # self.status = "Not complete"

    def __repr__(self):
        #What I want the user to see when printed out?
        return f"{self.name}: {self.due_date}"

#I need to create a todo class to store a lot of information about todos
#Best way to model the todo? A string is not good choice b/c you can't put name, due date, status, etc in a string, list, or dictionary. A todo has attributes and behaviors so a class the best option to store all of this data. 
