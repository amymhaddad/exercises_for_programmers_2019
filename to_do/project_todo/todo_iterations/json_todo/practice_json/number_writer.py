
import json
numbers = [2, 3, 5, 7, 11, 13]

#filename to store the list of numbers. It's customary to use '.json' to indicate taht the data in the file is stored in json format.
filename = 'numbers.json'

#use 'w' to write the data to teh file
with open(filename, 'w') as f_object:
    #use json.dump to store numbers in file
    json.dump(numbers, f_object)

