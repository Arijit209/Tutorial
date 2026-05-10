'''
mutable     -> changing the value
unordered   -> maintain the sequesnce element, cannot access with index value
hetrogenous -> multiple datatype save into the list [string, numbers, tuple]
note : create in curly bracket, must have only value into the curly bracket
'''
a =  {12, 16, 17, 13, 14 ,14}
b =  {10, 11, 12, 14 ,14}

########################################### List Traversing And Methods ##############################
## Traverse (show random value)
for i in a:
    print(i)

## Method
'''
add                  -> a.add(6)
remove               -> a.remove(6)
discard
pop                  -> a.pop() (pop a random element)
clear                -> a.clear() (clear all data)
union                -> a.union(b) or a|b (common show once)
intersection         -> a.intersection(b) or a&b (show only common element)
difference           -> a.difference(b) or a-b (diffrence value a from b)
semmetric difference -> a.symmetric_difference(b) or a^b (remove common part only and take others)
'''

print(a|b)
print(a&b)
print(a-b)
print(a^b)
