"""Create a program that reads in a file and counts the frequency of words in the file. Then construct a histogram displaying the words and the frequency"""

import csv
FILENAME = 'text.py'

def word_and_freq(FILENAME):

    """Read in text from a file; add each word and its frequency to dictionary"""

    counter = {}
    with open(FILENAME, newline='') as csvfile:
        linereader = csv.reader(csvfile, delimiter=' ')
        for row in linereader:
            for word in row:
                counter[word] = counter.get(word, 0) + 1
    return counter

word_counter = word_and_freq(FILENAME)

def show_freq(word_counter):

    """Create historgram dislaying the words and their frequncy from the dictionary"""

    template = ''
    for word, freq in word_counter.items():
        template += word + ': ' + '*' * freq + ' \n'
    return template.strip()

print(show_freq(word_counter))
