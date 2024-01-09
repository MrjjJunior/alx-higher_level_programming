#!/usr/bin/python3
''' Define a text writing funtion.'''

def write_file(filename="", text=""):
    '''
    Write content to a text file

    Args:

        filename (str): The name of the file to write to.

        text (str): The text to write to the file.

    Returns:
        The number of characters written.        


    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

