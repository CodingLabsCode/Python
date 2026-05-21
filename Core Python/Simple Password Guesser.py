from random import choice
from string import ascii_letters, digits
from time import sleep

chars = ascii_letters + digits
count = 16
attempts = 0

password = input("Enter Password\n");sleep(0.3)
computer_guess = ""

print("\nCracking password\n");sleep(0.5)

while computer_guess != password:
    computer_guess += choice(chars)
    count -= 1
    attempts += 1

    if count == 0:
        count = 16
        computer_guess = ""


print(f"Password: {computer_guess} | Tries: {attempts}")
