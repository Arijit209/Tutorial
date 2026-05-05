'''
    Modules and Packages
    A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py added. 
        Within a module, the module’s name (as a string) is available as the value of the global variable __name__. A package 
        is a way of structuring Python’s module namespace by using “dotted module names”.
        For example, the module name A.B designates a submodule named B in a package named A. Just like the use of modules saves the 
        authors of different modules from having to worry about each other’s global variable names, the use of dotted module names 
        saves the authors of multi-module packages from having to worry about each other’s module names.
    1. Importing Modules:
        You can import a module using the import statement. For example, to import the math module, you can use: import math.
    2. Importing Specific Functions or Variables:
        You can also import specific functions or variables from a module using the from keyword. For example, to import the sqrt 
        function from the math module, you can use: from math import sqrt.
    3. Aliasing Modules:
        You can also create an alias for a module using the as keyword. For example, to import the math module with the alias m, 
        you can use: import math as m.
    4. Creating Packages:
        To create a package, you need to create a directory and include an __init__.py file in that directory. The __init__.py 
        file can be empty, but it indicates that the directory is a package. You can then create modules within that package by 
        adding .py files to the directory.
    5. Importing from Packages:
        You can import modules from a package using the same import syntax as for regular modules. For example, if you have 
        a package named mypackage with a module named mymodule, you can import it using: import mypackage.mymodule.
    6. Using the sys Module:
        The sys module provides access to some variables used or maintained by the Python interpreter and to functions that 
        interact strongly with the interpreter. For example, you can use sys.path to get a list of directories that the interpreter searches for modules.
    7. Using the os Module:
        The os module provides a way of using operating system dependent functionality like reading or writing to the file system. 
        For example, you can use os.listdir() to get a list of files in a directory.
    8. Using the datetime Module:
        The datetime module provides classes for manipulating dates and times. For example, you can use datetime.datetime.now() 
        to get the current date and time.
    9. Using the random Module:
        The random module provides functions for generating random numbers and making random selections. For example, you can use 
        random.randint(1, 10) to generate a random integer between 1 and 10.
    '''
    
# Example of importing a module
import math
print(math.sqrt(16))  # Output: 4.0

# Example of importing specific functions from a module
from math import sqrt
print(sqrt(25))  # Output: 5.0

# Example of creating an alias for a module
import math as m
print(m.sqrt(36))  # Output: 6.0

# Example of using the sys module
import sys
print(sys.path)  # Output: List of directories that the interpreter searches for modules

# Example of using the os module
import os
print(os.listdir('.'))  # Output: List of files in the current directory

# Example of using the datetime module
import datetime
print(datetime.datetime.now())  # Output: Current date and time

# Example of using the random module
import random
print(random.randint(1, 10))  # Output: Random integer between 1 and 10

# Assuming we have a package named mypackage with a module named mymodule, we can import it as follows:
# import mypackage.mymodule

