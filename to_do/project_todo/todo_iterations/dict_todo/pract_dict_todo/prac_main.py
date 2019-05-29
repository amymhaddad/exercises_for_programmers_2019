from prac_todolist import ToDoList
import csv
import sys

def get_list_name():
    print("Enter you todo list information when prompted. Type 'q' to quit.")
    list_name = input("Enter your todo list name: ")
    return ToDoList(list_name)

def get_user_todos():
    user_todo_list = get_list_name()

    while True:
        print('\n')
        todo = input("Enter a todo name: ")
        if todo == 'q':
            break
        
        due_date = input("Enter a due date: ")
        if due_date == 'q':
            break
        
        status = input("Enter the todo status, otherwise hit return and the status will default to \'not started\': ")
        if status == 'q':
            break
        
        else:
            user_todo_list.add_todos(todo, due_date, status)
  
    return user_todo_list.dict_todos

print(get_user_todos())

def write_todos_csv():
    todo_details = get_user_todos()

    todo = todo_details.todos_dict[get_list_name()]
    print(todo)
write_todos_csv()

# todo = ToDoList.dict_todos[self.list_name]

    

#     with open(filename, mode='w', newline='') as csvfile:
#         fieldnames = ['list']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         writer.writerow(todo_details)        

# write_todos_csv(sys.argv[1])


 
# with open(filename, 'w', newline='') as csvfile:  
#         #fieldnames takes in keys. My key is an id Number. So I want to read in what all of the todo details are, which are stored as values in teh dictionary.
#         fieldnames = [num for num in range(1, number)]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()    
#         writer.writerow(todo_details)

      
        
