import csv
import sys
from todolist import ToDoList

def get_listname():
    print("Enter todo information when prompted. Type 'q' to quit.")
    list_name = input("Enter a todo list name: ")
    return ToDoList(list_name)


def add_todos_to_list():
    list_name = get_listname()

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
            list_name.add_todos(todo, due_date, status)

    return ToDoList.todos_dict


def write_todos_to_csv(filename):
    add_todos_to_list()
    number = ToDoList.todo_list_id
    todo_details = ToDoList.todos_dict
 
    with open(filename, 'w', newline='') as csvfile:  
        #fieldnames takes in keys. My key is an id Number. So I want to read in what all of the todo details are, which are stored as values in teh dictionary.
        fieldnames = [num for num in range(1, number)]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()    
        writer.writerow(todo_details)
        #This workd when hardcoding 
        # writer.writerow({"Todo Name": 'work', "Due Date": "May", "Status": "Done"})



        # for data in todo_details:
        #     writer.writerow(data)
     
write_todos_to_csv(sys.argv[1])



# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({


#this works if I just want to write the dict with out the header
    # with open(filename, 'w') as csvfile:    
    #     linewriter = csv.writer(csvfile)
    #     linewriter.writerows(todo_details)
