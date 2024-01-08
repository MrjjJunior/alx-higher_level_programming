#!/usr/bin/python3
""" Define an object attribute lookup function. """

def lookup(obj):
    """ Return a list of an object's available attribute. """
    
    return (dir(obj))
