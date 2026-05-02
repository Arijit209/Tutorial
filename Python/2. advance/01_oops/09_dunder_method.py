'''
    this is special method in python, start and end with __
'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'how are you'
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age
        return f'your sum of ages are {self.age + sum}'

obj = Animal('Lion', 12)
obj1 = Animal('Dolphin', 18)
obj2 = Animal('Tiger', 22)
print(obj + (obj1,))
print(obj + (obj1, obj2))
