#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = "New"
       

    @property
    def brand(self):
        """The brand property"""
        return self._brand
    @property
    def size(self):
        """The size property"""
        return self._size
    @property
    def condition(self):
        """The condition property"""
        return self._condition
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"
        
shoe = Shoe("Nike", 10.5)
shoe.brand
shoe.size
shoe.cobble()
shoe.condition