"""Get user input to create a todo list with todos"""

from todolist import ToDoList

def user_list_name():
    """Get user input for todo list name"""

    list_name = input("Enter a todo list name: ")
    return ToDoList(list_name)

def user_todos():
    """Get user input for todos and todo details"""

    list_name = user_list_name()
    print("Enter the todo information when prompted. Type 'q' to quit.\n")

    while True:
        todo = input("Enter a todo name: ")
        due_date = input("Enter a due date: ")

        if todo == 'q' or due_date == 'q':
            return list_name
            break
        else:
            list_name.add_todo(todo, due_date)

print(user_todos())
