#!/usr/bin/python3
# This file defines a Rectangle class with width and height

class Rectangle:
    # Initialize the Rectangle with optional width and height
    def __init__(self, width=0, height=0):
        self.width = width  # Set width using the property setter
        self.height = height  # Set height using the property setter

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # Check if value is integer
            raise TypeError("width must be an integer")
        if value < 0:  # Check if value is non-negative
            raise ValueError("width must be >= 0")
        self.__width = value  # Set the private width attribute

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # Check if value is integer
            raise TypeError("height must be an integer")
        if value < 0:  # Check if value is non-negative
            raise ValueError("height must be >= 0")
        self.__height = value  # Set the private height attribute
