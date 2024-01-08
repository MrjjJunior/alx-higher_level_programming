#!/usr/bin/python3
''' DEfine a class checking Function '''

def is_same_class(obj, a_class):
    '''
    Check if an is an instance of a given class
    
    Args:

        obj (any): The object to be checked.

        a_class (type): The class to match the obj.

    Return:

        if obj is an instance of a_class - True.
        else - Flase
    '''

    if type(obj) == a_class:
        return True
    return False
