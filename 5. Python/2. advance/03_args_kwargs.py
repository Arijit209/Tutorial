'''Args and Kwargs in Python
    In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
    *args allows you to pass a variable number of non-keyword arguments to a function. It is represented by an asterisk (*) 
    followed by the name of the parameter.
    **kwargs allows you to pass a variable number of keyword arguments to a function. It is represented by two asterisks (**) 
    followed by the name of the parameter.
    Here is an example to illustrate the use of *args and **kwargs:
'''
# #Args
# def addition(*args):
#     total = sum(args)
#     print(f'The sum of {args} is {total}')

# # addition(5, 10)  # This will work fine and print the sum of 5 and 10.
# addition(5, 10, 15, 20)  # This will work fine and print the sum of all the arguments.

# #Kwargs
# def information(**kwargs):
#     print("Information:")
#     for i in kwargs:
#         print(f'{i}: {kwargs[i]}')  
    
# information(name="Alice", age=25, city="New York")  # This will work fine

#Use case of both *args and **kwargs together in the decorator function
def decorate(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper

@decorate
def addition(a, b):
    print(f'The sum of {a} and {b} is {a + b}')
addition(5, 10)  # This will raise an error because the wrapper function does not accept any arguments.