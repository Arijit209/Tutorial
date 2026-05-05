'''
immutable   -> cannot changing the value
duplicates  -> use duplicate values
ordered     -> maintain the sequesnce element, access with index value
hetrogenous -> multiple datatype save into the list
note : create in first bracket
'''

a =  (12, 13, 14 ,14)
# print(a[0]) # Indexing
# print(a[0:2]) # Slicing

########################################### List Traversing And Methods ##############################
## Traverse
## 1st Way Using Index 
# for i in range(len(a)):
#     print(a[i])

## 2nd Way Direct Value Access
# for i in a:
#     print(i)

## Method (only this two allow)

# Find the index
index = a.index(13)
print(index)

# Find the duplicate occurance with count
count = a.count(14)
print(count)

# Tupple can unpacking the value
a,b,c,d,e = (1,2,3,4,5)
print(a,b)

# Note: diffrent between tuple an integer
a = (1)
print(type(a)) # integer

b = (1,)
print(type(b)) # tuple