#!/usr/bin/python3
''' defines a function that reads text files '''

def read_file(filename=""):
    """ Prints contents of a UTF8 text file to stdout """

    with open('my_file_0.txt', 'r') as f:
        print(f.read(), end="")
