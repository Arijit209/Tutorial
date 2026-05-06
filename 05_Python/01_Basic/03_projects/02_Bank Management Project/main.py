'''
    Bank Account Management System
     -Banck Account
     -Deposit Money
     -Withdraw Money
     -Details of Account
     -Update Account Details
     -Delete Account
'''
import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists() and Path(database).is_file():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            print("No data file found. Starting with an empty database.")
    except Exception as e:
        print("Error loading data:", e)


    def createAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo": Bank.__accountGenerate(),
            "balance": 0
        }
        if info["age"] < 18 or len(str(info["pin"])) != 4 or not str(info["pin"]).isdigit():
            print("You must be at least 18 years old to create an account.")
        else:
            print('Account created successfully!')
            for i in info:
                print(f"{i.capitalize()}: {info[i]}")
            print("Please keep your account number and pin safe.")
            Bank.data.append(info)
            Bank.__update()

    def depositMoney(self):
        acconno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        userdata = [i for i in Bank.data if i["accountNo"] == acconno and i["pin"] == pin]
        
        if userdata == False:
            print("Invalid account number or pin.")
        else:
            amount = int(input("Enter the amount to deposit: "))
            if amount > 10000 or amount <= 0:
                print("Invalid amount. You can only deposit up to 10000 at a time.")
            else:
                userdata[0]["balance"] += amount
                Bank.__update()
                print(f"Amount deposited successfully! Your new balance is: {userdata[0]['balance']}")
        
    def withdrawMoney(self):
        acconno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        userdata = [i for i in Bank.data if i["accountNo"] == acconno and i["pin"] == pin]
        
        if userdata == False:
            print("Invalid account number or pin.")
        else:
            amount = int(input("Enter the amount to withdraw: "))
            if amount > userdata[0]["balance"]:
                print("Insufficient balance.")
            elif amount > 10000 or amount <= 0:
                print("Invalid amount. You can only withdraw up to 10000 at a time.")
            else:
                userdata[0]["balance"] -= amount
                Bank.__update()
                print(f"Amount withdrawn successfully! Your new balance is: {userdata[0]['balance']}") 
    
    def viewAccountDetails(self):
        acconno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        userdata = [i for i in Bank.data if i["accountNo"] == acconno and i["pin"] == pin]
        
        if userdata == False:
            print("Invalid account number or pin.")
        else:
            print("Account Details:")
            for i in userdata[0]:
                print(f"{i.capitalize()}: {userdata[0][i]}")
                
    def updateAccountDetails(self):
        acconno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        userdata = [i for i in Bank.data if i["accountNo"] == acconno and i["pin"] == pin]
        
        if userdata == False:
            print("Invalid account number or pin.")
        else:
            print("What do you want to update?")
            print("Press 1 to update name")
            print("Press 2 to update email")
            print("Press 3 to update pin")
            check = int(input("Enter your choice: "))
            
            if check == 1:
                print(f"Your current name is: {userdata[0]['name']}")
                newname = input("Enter your new name: ")
                userdata[0]["name"] = newname
                Bank.__update()
                print("Name updated successfully!")
            elif check == 2:
                print(f"Your current email is: {userdata[0]['email']}")
                newemail = input("Enter your new email: ")
                userdata[0]["email"] = newemail
                Bank.__update()
                print("Email updated successfully!")
            elif check == 3:
                print(f"Your current pin is: {userdata[0]['pin']}")
                newpin = int(input("Enter your new pin: "))
                if len(str(newpin)) != 4 or not str(newpin).isdigit():
                    print("Invalid pin. Pin must be a 4-digit number.")
                else:
                    userdata[0]["pin"] = newpin
                    Bank.__update()
                    print("Pin updated successfully!")
            else:
                print("Invalid choice.")
    
    def deleteAccount(self):
        acconno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        userdata = [i for i in Bank.data if i["accountNo"] == acconno and i["pin"] == pin]
        
        if userdata == False:
            print("Invalid account number or pin.")
        else:
            check = input("Are you sure you want to delete your account? (yes/no): ")
            if check.lower() != "yes":
                print("Account deletion cancelled.")
                return  
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("Account deleted successfully!")
    
    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(cls.data))
            
    @classmethod
    def __accountGenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices('@#$%^&*!()', k=1)    
        id = alpha + num + spchar
        random.shuffle(id)
        return ''.join(id)
    
user = Bank()

print("Welcome to Bank Account Management System")
print("Press 1 to Create Account")
print("Press 2 to Deposit Money")
print("Press 3 to Withdraw Money")
print("Press 4 to View Account Details")
print("Press 5 to Update Account Details")
print("Press 6 to Delete Account")

check = int(input("Enter your choice: "))

if check == 1:
    user.createAccount()
if check == 2:
    user.depositMoney()
if check == 3:
    user.withdrawMoney()
if check == 4:
    user.viewAccountDetails()
if check == 5:
    user.updateAccountDetails()
if check == 6:
    user.deleteAccount()