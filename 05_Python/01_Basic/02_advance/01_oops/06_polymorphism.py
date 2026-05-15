'''
    It allows the same interface or method name behafe differently depending on the object or context
    -Method Overriding 
    -Method Overloading (not exist in python)(same method name but different arguments)
    -Duck Typing 
'''
##Method Overriding
# class Animal:
#     def show(self):
#         print('Hello I am Arijit')

# class Human(Animal):
#     def show(self):
#         print('How are you')

# obj = Human()
# obj.show() #How are you

##Duck Typing
class Animal:
    def show(self):
        print('Hello I am Arijit')

class Human:
    def show(self):
        print('How are you')

obj = Animal()
obj1 = Human()
obj.show()
obj1.show()