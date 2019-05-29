
import json

#This is the file I'm reading in
filename = 'numbers.json'

with open(filename) as f_object:
    #Use json.load() to LOAD the info stored in numbers.json and store this info in a variable 
    numbers = json.load(f_object)

print(numbers)
