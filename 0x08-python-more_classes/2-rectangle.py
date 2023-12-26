#!/usr/bin/python3

"""
definition of class Rectangle.
"""

class Rectangle:
    """ representation """
    def __init__(self, width=0, height=0):
        """initalizing the values"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter for the privete width """
        return self.__width
    @width.setter
    def width(self, value):
        """setter for the private width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """ getter for the privete height """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2) 
