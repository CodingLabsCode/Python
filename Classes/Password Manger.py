from time import sleep as s
from time import time

passwords = []

class Password():
    def __init__(self, app, password):
        self.app = app
        self.password = password

    def Pass(self):
        print(f"App:{self.app} | Password:{self.password}")

def showPass():
    if len(passwords) == 0: print("You Have No Passwords Yet")
    else: 
        for i, password in enumerate(passwords, start=1):
            print(f"{i}:",end="")
            password.Pass()
    input("Press Enter to Contiune: ")
def addPass():
    app = input("Enter App Name: ");s(0.5)
    password = input("Enter Password: ");s(0.5)
    passes = Password(app, password)
    passwords.append(passes)
    print("Password Added")
def removePass():
    remove = int(input("Remove Password (Enter 1 e.g): "));s(0.3)
    passwords.pop(remove - 1)
    print("Password Removed")
def accountStats():
    print(f"=== {userName}s Stats ===\n"
          f"Amount Of Passwords: {len(passwords)}\n"
          f"Amount Of Time On Password Manager: {startTime} Seconds \n")
    input("Press Enter To Contiune: ")
userPinMake = input("Make A Pin: ")
pin = userPinMake
userName = input("Enter a Username: ")
userPin = input("Enter Your Pin: ")
while userPin != pin:
    print("Try Again")
    userPin = input("Enter Your Pin: ")
print("Acess Granted");startTime = time()

while True:
    user = input("=== Password Manager ===\n"
                 "(1)Add Password\n"
                 "(2)View Passwords\n"
                 "(3)Remove Passwords\n"
                 "(4)View Account\n"
                 "(5)Exit\n"
                 "Enter Choice: ");s(1)
    
    match user:
        case "1":
            addPass()
        case "2":
            showPass()
        case "3":
            removePass()
        case "4":
            accountStats()
        case "5":
            print("Goodbye")
            exit()
        case _:
            print("Only 1-4")
