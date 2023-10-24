#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Instantiation with size
        :param size:
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
