'''
    A contructor is a method that runs automatically when we call a class 
    and this contructor function will target the objects location
    self is use for particular location when object create
'''
## Create a class
class Person:
    def __init__(self, hand, noise, leg):
        self.hand = hand
        self.noise = noise
        self.leg = leg
    def show(self):
        print(f'your object details are {self.hand}, {self.noise}, {self.leg}')

black = Person(2,1,2)
white = Person(2,1,1)

black.show()
white.show()