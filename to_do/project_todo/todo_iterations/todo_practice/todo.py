class ToDo():

    def __init__(self, name, due_date='TBD'):
        self.name = name
        self.due_date = due_date
    
    def __repr__(self):
        return f"{self.name}: {self.due_date}"

