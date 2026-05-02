'''
mutable     -> changing the value
duplicates  -> use duplicate values
ordered     -> maintain the sequesnce element, access with index value
hetrogenous -> multiple datatype save into the list
note : create in square bracket
'''

a =  [12, 13, 14 ,14]
# print(a[0]) # Indexing
# print(a[0:5]) # Slicing

########################################### List Traversing And Methods ##############################
## Traverse
## 1st Way Using Index 
# for i in range(len(a)):
#     print(a[i])

## 2nd Way Direct Value Access
# for i in a:
#     print(i)

## Method
## Append (Enter into last)
a.append(6)
print(a)

## Insert (Insert into particular index)
a.insert(2, 4)
print(a)

## Remove (First occuranse is remove)
a.remove(4)
print(a)

## Copy (copy one to another)
b = a # deep copy where in change b, a also change
print(b)

b = a.copy() # shallow copy where in change b, a not change
print(b)

## Find the largest number
l = [12, 36, 14, 19, 128, 33]
largest = l[0]
index = 0
for m in range(len(l)):
    if l[m] > largest:
        largest = l[m]
        index = m

print(f'your largest number is {largest} and ithe index number is {index}')

## Find the second largest number
largest1 = l[0]
secondlargest1 = l[0]
index1 = 0
for n in range(len(l)):
    if l[n] > largest1:
        secondlargest1 = largest1
        largest1 = l[n]
        index1 = n

print(f'your largest number is {secondlargest1}')


