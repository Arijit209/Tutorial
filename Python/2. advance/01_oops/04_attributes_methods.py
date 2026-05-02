'''
    Attributes
    -Class Attribute
    -Instance Attribute
'''
class Animal:
    name = 'Lion' #Class Attribute

    def __init__(self, age):
        self.age = age #Instance Attribute

'''
    Method
    -Instance Method
    -Class Method
    -Static Method
'''
class Animal:
    def __init__(self, age):
        self.age = age #Instance Attribute

    def show(self): #Instance Method
        print(f'the age is {self.age}')
    
    @classmethod
    def hello(cls): #Class Method
        print('this is class method and its target class location')

    @staticmethod
    def static(): #Static Method
        print('this is static method')

obj = Animal(38)
obj.show()
obj.hello()
obj.static()