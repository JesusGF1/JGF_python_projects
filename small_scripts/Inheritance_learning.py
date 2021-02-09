# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:31:58 2021

@author: jesus
"""

class Shape():
    def __init__(self):
        pass
    
    def what_am_i(self):
        print("I am a shape")
        

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    
cuadrado = Square(2)
print(cuadrado.calculate_perimeter())
cuadrado.what_am_i()