'''
mutable             -> changing the value, not index key change
duplicates          -> use duplicate values but ndex not change
insertion-ordered   -> maintain the sequesnce element, cannot access with index value
hetrogenous         -> multiple datatype save into the list [string, numbers, list, dictionary]
note : create in curly bracket, must have key and value pair into the curly bracket
'''
a =  {10:100, 20:200, 30:300, 40:400}
print(a[40])
a[30] = 3000
print(a)
'''
CRUD
create -> a[50] = 500
read   -> a[40]
update -> a.update(50: 500) or a[30] = 3000
delete -> del a[50]
'''

########################################### List Traversing And Methods ##############################
## Traverse
for i in a:
    print(a[i])

for i in a.values():
    print(i)

## Method
## Method
'''
clear                -> a.clear() (clear all data)
copy                 -> a.copy() (shallow copy mean if change one not change another)
get                  -> a.get(20)
items                -> a.items()

'''

d1 = {10:100, 20:200, 40:300}
d2 = {40:400, 50:500, 60:600}

for i in d2:
    d1[i] = d2[i]
print(d1)

## Find a frequency in the list

a = [1,1,1,1,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,5,5]
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)
