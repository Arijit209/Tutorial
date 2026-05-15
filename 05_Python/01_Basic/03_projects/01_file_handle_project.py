from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f'{i} : {items}')

def createFile():
    try:
        readFileAndFolder()
        name = input(f'please tell your file name: ')
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p,"w") as fs:
                data = input(f'what you want to write in this file: ')
                fs.write(data)
            print('File created successfully')
        else:
            print('This file already exist')
    except Exception as err:
        print(f'An error occur {err}')

def readFile():
    try:
        readFileAndFolder()
        name = input(f'which file you want to read: ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print(f'Read is successfully')
        else:
            print('The file does not exist')
    except Exception as err:
        print(f'An error occur {err}')

def updateFile():
    try:
        readFileAndFolder()
        name = input(f'Tell which file you want to update: ')
        p = Path(name)
        if p.exists() and p.is_file():
            print('press 1 for changing the name of the file')
            print('press 2 for overwriting the data of the file')
            print('press 3 for appending some content of the file')
            res = int(input(f'Tell you response: '))
            if res == 1:
                name2 = input(f'Tell your new file name: ')
                p2 = Path(name2)
                p.rename(p2)
            print('Your file rename successfully')
            if res == 2:
                with open(p,"w") as fs:
                    data = input(f'Tell what you want to write this is overwrite the data: ')
                    fs.write(data)
            print('Your data overwrite successfully')
            if res == 3:
                with open(p,"a") as fs:
                    data = input(f'Tell what you want to write this is append the data: ')
                    fs.write(data)
            print('Your data append successfully')

    except Exception as err:
        print(f'An error occur {err}')

def deleteFile():
    try:
        readFileAndFolder()
        name = input(f'Which file you want to delete: ')
        p = Path(name)
        if p.exists() and p.is_file:
            os.remove(p)
            print('File remove successfully')
        else:
            print('No file found')
    except Exception as err:
        print(f'An error occur {err}')

print('Press 1 for craeting a file')
print('Press 2 for reading a file')
print('Press 3 for updating a file')
print('Press 4 for deleting a file')

check = int(input(f'Please tell your response: '))

if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
else:
    deleteFile()