"""Get user input to create a todo list with todos"""

from todolist import ToDoList

def user_list_name():
    """Get user input for todo list name"""
    
    print("Enter the todo information when prompted. Type 'q' to quit.\n")

    list_name = input("Enter a todo list name: ")
    if list_name != 'q':
        return ToDoList(list_name)

def user_todos():
    """Get user input for todos and todo details"""

    list_name = user_list_name()

    while True:
        todo = input("Enter a todo name: ")
        if todo == 'q':
            return list_name
            break

        due_date = input("Enter a due date: ")
        if due_date == 'q':
            return list_name
            break
        else:
            list_name.add_todo(todo, due_date)

print(user_todos())
