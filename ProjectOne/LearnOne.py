import time
from random import randint

print("What is your first name?")
first_name = input()
print("What is your last name?")
last_name = input()

print("What is your email for the account?")
email = input()

print("Your email is", email, "— is this correct?")
answer = input()
if answer.lower() == "yes":
    print("Great, let's continue!")
else:
    print("Let's try again later.")

password = "coneman"
while True:
    print("What is your password?")
    answer = input()
    if answer == password:
        print("That is right, let's continue")
        break
    else:
        print("That's incorrect")

print("Security question: what is your favourite colour?")
fav_colour = input()

print("What is your current age?")
current_age = input()
age = int(current_age)
print("You are", age, "and called", first_name)
if age > 18:
    print("You are a grown adult")
elif age > 13:
    print("You are an annoying teenager")
else:
    print("You are a little child, get off the phone")

guesses = 0
while guesses < 3:
    answer = input("Say the magic word: ")
    if answer == "YIPIEE":
        print("Yipeeee you got it right boy, come on in 🎉")
        break
    else:
        guesses += 1
        if guesses < 3:
            print("Oh bro you got it wrong, you have", 3 - guesses, "more chance(s) — you can do it 💪")
        else:
            print("Too many tries! Locked out 🚫")
            time.sleep(600)  # 10 minutes


rand_num = randint(11,99)
print("To Prove That Your Not A Robot Please Type", rand_num)
rand_guess = int(input())
if rand_num == rand_guess:
    print("Access Granted🔓")
else:
    print("You Are A Robot Bye Bye🔒")
    exit()

print()
print("Would you like to buy a starter pack?")
print("For the cost of £1.99?")
print("Please answer with -Yes- or -No-")
answer = input()
answer = answer.lower()

print("\n📋 Profile Summary:")
print("Name:", first_name, last_name)
print("Age:", age)
print("Favourite colour:", fav_colour)
print("Email:", email)
