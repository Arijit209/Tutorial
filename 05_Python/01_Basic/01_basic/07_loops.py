###########################################For Loop############################################
# range(start, stop, steps)

# Front Direction
# a = range(1,20,2)
# for i in a:
#     print(i)

# for b in range(1,20,3):
#     print(b)

# for c in range(22):
#     print(c)

# for d in range(20, 51):
#     print(d)

# Reverse Direction
# for e in range(16, 0, -1):
#     print(e)

# for f in range(-5, -16, -1):
#     print(f)

# n = int(input('Please input your table number '))
# m = (n*10)+1
# for g in range(n, m, n):
#     print(g)

## String
# a = "ARIJIT"
# for h in range(len(a)):
#     print(a[h])

# a = "ARIJIT DUTTA"
# for j in a:
#     print(j)

## Break
# for k in range(1, 21):
#     if k == 15:
#         break
#     print(k)

## If break is not executed then else executed otherwise break executed
# for kk in range(11, 21):
#     if kk == 15:
#         print('break statement is executed')
#         break
#     print(kk)
# else:
#     print('break statement is not executed')

## Continue
# for l in range(1, 21):
#     if l == 15:
#         continue
#     print(l)

## Example 
# str = "Absdk237623%$#^%$^&jsdhk564$#%#"
# digit = 0
# char = 0
# sym = 0
# for m in str:
#     if m.isdigit():
#         digit += 1
#     elif m.isalpha():
#         char += 1
#     else:
#         sym += 1
# print(f"your digit is {digit}, character is {char}, symbol is {sym}")

##########################################While Loop#########################################
# a = 1
# while a <= 30:
#     print(a)
#     a += 1

# b = 256
# while b > 0:
#     print(b%10)
#     b = b//10

# c = 256
# rev = 0
# while c > 0:
#    rev = (rev * 10) + (c % 10)
#    c = c // 10

# print(rev)
