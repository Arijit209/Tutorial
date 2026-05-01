##############################################String#######################################
# Hello world print show
print('hello world')
print("hello world")

# Inverted comma
print("I'm fine")
print('I"m fine')

# Quotation
print('Arijit\'s "Laptop"')

# Multiple Times Write same string
print('Arijit ' * 5)

# Path Show
print('C:\\Windows\\System32\\cmd.exe')
print(r'C:\Windows\System32\cmd.exe')

# Concat String
fname = 'Arijit '
lname = 'Dutta'
print(fname)
print(lname)
print(fname + lname)

# Indexing and Length Found
name = 'Arijit'
print(name[3])
print(name[-1])
print(len(name))

# String Slicing
print(name[1:3:1]) #star-point:end_point:steps

########################################Type Conversion#######################################
# Explicit Conversion
'''
int()
float()
str()
bool()

'''
# Integer to String
a = 12
b = str(a)
print(type(a))
print(type(b))

# String to Integer
c = '12'
d = int(c)
print(type(c))
print(type(d))

# String/Integer to Boolean
'''
False value 7 types we get
    False,
    0,
    0.0,
    "",
    [],
    (),
    {},
'''
e = 'Arijit'
f = bool(e)
print(type(e))
print(type(f)) 

g = 1
h = bool(g)
print(type(g))
print(type(h)) 

# Implicit Conversion
a = 12/3
print(a)
print(type(a))



