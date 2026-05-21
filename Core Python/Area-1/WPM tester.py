from time import time as t
from time import sleep as s
from random import choice as c
count = 6
w = ["or ", "word ", "house ", "home ", "and ", "dad ", 
        "interest ", "if ", "count ", "text ", "mouse ", 
        "rat ", "mice ", "user ", "me ", "mum ", "nan ",
        "start ", "else ", "bed ", "time ", "new ",
         "own ", "head ", "open ", "very ", "to ",
          "mean ", "hand ", "people ", "other ", "old ",
           "still ", "take ", "set ", "eye ", "by ", "he "  ]

text = ""

userInput = int(input("(1)EASY\n(2)MEDIUM\n(3)HARD\nChoose Mode"))

match userInput:
    case 1:
        print("Easy Mode Chosen"); mode = "Easy"
        for i in range(5):
            words = c(w)
            text += words
    case 2:
        print("Medium Mode Chosen"); mode = "Medium"
        for i in range(10):
            words = c(w)
            text += words
    case 3:
        print("Hard Mode Chosen"); mode = "Hard"
        for i in range(20):
            words = c(w)
            text += words

print(text)
input("Press Enter To Start: ")

for i in range(5):
    count -= 1
    print(count);s(1)

start = t()
user = input("> ")
end = t()

time_taken = end - start

words = len(user.split())
wpm = words / (time_taken / 60) 

print(f"WPM {round(wpm, 2)} You did it on {mode}")
