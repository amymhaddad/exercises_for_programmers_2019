
filename = 'text.py'
import csv

def word_and_freq(filename):
    counter = {}
    with open(filename, newline='') as csvfile:
        linereader = csv.reader(csvfile, delimiter=' ')
        for row in linereader:
            for word in row:
                counter[word] = counter.get(word, 0) + 1
    return counter

word_counter = word_and_freq(filename)

def show_freq(word_counter):
    template = ''
    for word, freq in word_counter.items():
        template += word + ': ' + '*' * freq + ' \n'
    return template.strip()            

print(show_freq(word_counter))
