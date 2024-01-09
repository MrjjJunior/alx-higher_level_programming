#!/usr/bin/python3
''' define a function that reads files '''

def read_file(filename=""):
    ''' Prints contents of my_file_0.txt'''

    with open('my_file_0.txt', 'r') as f:
        print(f.read(), end="")
