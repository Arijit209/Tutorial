'''
Decorators are a powerful feature in Python that allow you to modify the behavior of functions or classes. 
They are often used to add functionality to existing code without changing its structure. 
A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
In the example below, we have a simple class `Animal` with a method `show`. We will use the `@property` decorator to make the 
`show` method behave like an attribute
'''
class Animal:
    @property
    def show(self):
        print("I am an animal")

obj = Animal()
obj.show

def decorate(func):
    def wrapper(a, b):
        print("Before the function is called.")
        func(a, b)
        print("After the function is called.")
    return wrapper

@decorate
def addition(a, b):
    print(f'The sum of {a} and {b} is {a + b}')
addition(5, 10)  # This will raise an error because the wrapper function does not accept any arguments.

