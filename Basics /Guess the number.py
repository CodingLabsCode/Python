from random import randint 
from time import sleep
def easy(): global number; number = randint(1,5)
def medium(): global number; number = randint(1,10)
def hard(): global number; number = randint(1,20)
def rules(): print("EASY MODE: is numbers 1 to 5\nMEDIUM MODE: is numbers 1 to 10\nHARD MODE: is numbers 1 to 20");sleep(1);lobby()
def lobby():
    global index
    index = input("==== Guess The Number Game ====\n(1)Easy Mode\n(2)Medium Mode\n(3)Hard Mode\n(4)Rules\n");sleep(0.8)
guess = 3
lobby()

match index:
    case "1":easy(); mode = "Easy"
    case "2":medium(); mode = "Medium"
    case "3":hard(); mode = "hard"
    case "4":rules()
    case _: print("1,4 Only");sleep(0.5);lobby()

while guess != 0:
    while True:
        try:
            user = int(input("Guess a number: "));sleep(0.3)
            break
        except:
            print("Invaild Option")
    if user == number:
        print("Well done you got it right!!!!!")
        break
    elif user != number:
        choice = input("(1)Carry On\n(2)Hint!!!\n");sleep(0.5)
        guess -= 1
        match choice:
            case "1": continue
            case "2": 
                if user > number: print(f"{user} is Higher: ") ;sleep(0.5)
                else: print(f"{user} is Lower: ");sleep(0.5)
