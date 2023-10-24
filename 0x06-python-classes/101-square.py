#!/usr/bin/python3
""" Creates a class Square
"""


class Square:
    """
    creating square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor with instantiation
        of size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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
            print()
            return
        else:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """
            Return position
        :return:
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Used to set the position value
        :param value:
        :return:
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

        def __str__(self):
            """
            do just ike my_print function
            :param self:
            :return:
            """
            self.my_list = []
            if self.__size == 0:
                return ""
            for j in range(self.__position[1]):
                self.my_list.append("\n")
            for i in range(self.__size):
                self.my_list.append(" " * self.__position[0])
                self.my_list.append("#" * self.__size)
                if i < self.__size - 1:
                    self.my_list.append("\n")
            return "".join(self.my_list)
