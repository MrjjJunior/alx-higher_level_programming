#!/usr/bin/python3

"""Define the Square"""

class Square:
    """display square"""

    def __init__(self, size=0):
        """start a new square.
        Args:
            size: size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= ")
        self.__size = value

    def area(self):
        """ return the current area of the square"""
        return(self.__size * self.__size)
