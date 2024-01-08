#!/usr/bin/python3
""" Define  an inherited list class Mylist. """

class Mylist(list):
    """ Sorted list function """

    def print_sorted(self):
        """ Print a list in sorted ascending order. """
        print (sorted(self))
