#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """ Square Class
    """

    def __init__(self, size=0):
        """
        Constructor with instantiation
        of size
        """
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square
        area
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

    def my_print(self):
        """
        prints the square with character
        :return:
        """
        if self.size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
