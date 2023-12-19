#!/usr/bin/python3
"""Square"""

class Square:
    """show new square"""

    def __init__(self, size=0):
        
        """Start anew Square.
        Args:
            size(int): THe size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
