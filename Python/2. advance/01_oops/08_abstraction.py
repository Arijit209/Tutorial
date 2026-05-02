'''
    abstraction in not working in python
'''
from abc import ABC, abstractmethod

class abstract(ABC): #abstractclass
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        print('This is perimeter')
    def area(self):
        print('This is area')

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        print('This is perimeter')
    def area(self):
        print('This is area')

obj = Circle(7)
