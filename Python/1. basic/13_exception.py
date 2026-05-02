## Syntax Error
# print('Hello World'
      
## Indentation Error
# a = 12
# if a == 13:
# print('check')

## Tabs Error

## Exception Error
# a = int(input("Tell a number: "))
# print(10/a)
# print('End') # not run if exception occur in previous line

## Exception Handling
'''
try
except
else
finally
raise
'''
## try-except-else-finnaly
# try:
#     a = int(input("Tell a number: "))
#     print(10/a)
# except ZeroDivisionError:
#     print('Sorry you caanot do this')
# print('End')

# try:
#     a = int(input("Tell a number: "))
#     print(10/a)
# except Exception as err:
#     print(f'Sorry you caanot do this {err}')
# else:
#     print('run else block')
# print('End')

# try:
#     a = int(input("Tell a number: "))
#     print(10/a)
# except Exception as err:
#     print(f'Sorry you caanot do this {err}')
# else:
#     print('run else block')
# finally:
#     print('I am finally block')
# print('End')

## raise
age = int(input('Tell Your age: '))
try:
    if age < 10 or age > 18:
        raise ValueError('You are not eligible')
    else:
        print('welcome to join')
except Exception as err:
    print(f'Show this exception {err}')

print('the club will start soon')

