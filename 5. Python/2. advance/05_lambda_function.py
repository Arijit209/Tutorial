'''
    Lambda functions are small anonymous functions that can have any number of arguments but can only have one expression. 
    They are defined using the lambda keyword and are often used for short, throwaway functions that are not reused elsewhere 
    in the code. The syntax for a lambda function is: lambda arguments: expression
    1. Basic Syntax:
    The basic syntax of a lambda function is as follows: lambda arguments: expression
'''
def add(x, y):
    print(x + y)
    
add(5, 3)

# Example of a lambda function to add two numbers
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))

#if-else with lambda
is_even = lambda x: 'even' if x % 2 == 0 else 'odd'
print(is_even(5))
