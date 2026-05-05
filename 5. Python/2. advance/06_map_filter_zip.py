'''
Map, Filter, and Zip Functions
    The map, filter, and zip functions are powerful tools in Python that allow you to manipulate and process data in a functional 
    programming style. Here's a brief overview of each function: 
    1. Map Function:
        The map function applies a given function to each item of an iterable (like a list) and returns a map object 
        (which is an iterator). The syntax for the map function is: map(function, iterable)
    2. Filter Function:
        The filter function filters elements from an iterable based on a given function and returns a filter object 
        (which is an iterator). The syntax for the filter function is: filter(function, iterable)
    3. Zip Function:
        The zip function combines multiple iterables element-wise and returns a zip object (which is an iterator). 
        The syntax for the zip function is: zip(iterable1, iterable2, ...)
'''
# Example of using the map() function to square a list of numbers
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(doubled)

# Example of using the filter() function to filter out even numbers from a list
def even(x):
    if x % 2 == 0:
        return True
    return False
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(even, lists))
print(even_numbers)

result = list(filter(lambda x: True if x % 2 == 0 else False, lists))
print(result)

# Example of using the zip() function to combine two lists into a list of tuples
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zipped = list(zip(list1, list2))
print(zipped)