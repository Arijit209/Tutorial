'''
    In general terms inheritance means property or any pessession that comes to an heir
'''
class Animal: #this is parent class
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

class Dog(Animal): #Single inheritance and it child class
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def show(self):
        print(f'This is my show1 {self.name}')

dog1 = Dog(30, 'Arijit')
dog1.hello()
dog1.show()

class Cat(Animal, Dog): #Multiple inheritance and it child class
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name

    def show(self):
        print(f'This is my show1 {self.name}')

class Cow(Dog): #Multulevel inheritance and it child class
    def __init__(self, age, name, userid):
        super().__init__(age, name)
        self.userid = userid

    def show(self):
        print(f'This is my show1 {self.userid}')