import json

username = input("What's your name? ")
filename = 'username.json'

with open(filename, 'w') as f_object:
    #Use json.dump and pass the user_input and f_object to sreo int a file
    json.dump(username, f_object)

file_to_readin = 'numbers.json'

with open(file_to_readin, 'r') as f_object:
    info = json.load(f_object)
print(info)
