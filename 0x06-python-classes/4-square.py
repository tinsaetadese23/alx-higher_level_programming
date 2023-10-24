#!/usr/bin/python3
"""
Creates a class square
"""


class Square:
    """
    creating a square class
    """

    def __init__(self, size=0):
        """
        instantiating with size
        :param size:
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculating area
        :return:
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
       Get size
       :return: size
       """
        return self.__size

    @size.setter
    def size(self, value):
        """
       Set size
       :param self:
       :param value:
       :return: none
       """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > 0")
        self.__size = value
