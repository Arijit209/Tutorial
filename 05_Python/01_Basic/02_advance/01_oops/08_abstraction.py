'''
    abstraction is the process of hiding the implementation details and showing only functionality to the user.
    It allows us to focus on what the object does instead of how it does it.
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
print(obj.radius)
obj.perimeter()
obj.area()
