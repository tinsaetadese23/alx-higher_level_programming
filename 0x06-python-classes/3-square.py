#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """
    Creating Square Class
    """

    def __init__(self, size=0):
        """
        initialization with size
        :param size:
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculating area
        :return:
        """
        return self.__size * self.__size
