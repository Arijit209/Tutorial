'''
Comprehensions are a concise way to create lists, dictionaries, and sets in Python. They allow you to generate new collections 
by applying an expression to each item in an iterable, optionally filtering items using a condition.
1. List Comprehensions:
List comprehensions provide a compact syntax for creating lists. The basic syntax is: [expression for item in iterable if condition]
'''

a= 12
print('even') if a%2==0 else print('odd')

# Example of a list comprehension to create a list of even numbers from 1 to 20
l=[i for i in range(1, 21) if i % 2 == 0]
print(l)

# Example of a set comprehension to create a set of even numbers from 1 to 20
s={i for i in range(1, 21) if i % 2 == 0}
print(s)

# Example of a dictionary comprehension to create a dictionary of even numbers and their squares from 1 to 20
a={i : i**2 for i in range(1, 21) if i % 2 == 0}
print(a)




