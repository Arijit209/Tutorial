'''
    Access Modifier
        -public
        -protected (no need to use in python)
        -private
'''
##Public
# class Factory:
#     a = "Pune"
#     def show(self):
#         print('Hello i am pune factory')

# class Bhopal(Factory):
#     def show(self):
#         print(super().a)

# obj = Bhopal()
# obj.show()

##Protected
# class Factory:
#     _a = "Pune"
#     def show(self):
#         print('Hello i am pune factory')

# class Bhopal(Factory):
#     def show(self):
#         print(super()._a)

# obj = Bhopal()
# obj.show()

##Private
# class Factory:
#     __a = "Pune"
#     def __show(self):
#         print('Hello i am pune factory')

# class Bhopal(Factory):
#     def show(self):
#         print(super().__a)

# obj = Factory() #Access from child class
# print(obj._Factory__a)
# obj._Factory__show()

# obj1 = Bhopal() #Not access from child class
# obj1.show()