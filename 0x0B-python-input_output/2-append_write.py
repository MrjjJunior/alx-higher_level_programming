#!/usr/bin/python3
''' Defines function that appends to file '''

def append_write(filename="", text=""):
    '''
    Args:
        filename (str): The 
        text (str):
    Return:
        returns the file with text appended to it.
    '''

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
