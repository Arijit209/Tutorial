############################################If-Elif-Else-Statement###########################################
# If Statement
name = 'Arijit'
if (name == 'Arijit'):
    print('Name is found')

# If-Else Statement
age = 18
if (age >= 18):
    print('You are eligible voter')
else:
    print('Sorry!, you are under age')

# If-Elif-Else Statement
marks = 80
if (marks > 90):
    print('Grade A+')
elif (marks > 80):
    print("Grade A")
elif (marks > 70):
    print("Grade B")
elif (marks > 60):
    print("Grade C")
elif (marks > 50):
    print("Grade D")
else:
    print("You are fail")

# Ternary
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

num = -5
result = "Positive" if num > 0 else ("Zero" if num == 0 else "Negative")
print(result)
