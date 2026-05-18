from random import randint as r
from time import time as t
correct = 0
incorrect = 0
questions = int(input("How Many Qestions Would You Like: "))
beforeQuestions = questions
start = t()
while True:
    if questions == 0 :
       end = t()
       print(
           f"Time Taken {end - start:.2f}\n"
           f"{correct} Correct\n"
           f"{incorrect} Incorrect\n"
           f"{correct} / {beforeQuestions}"
       )
       break
    try:
        num1, num2 = r(2,12) , r(2,12)
        product = num1 * num2
        user = int(input(f"{num1} x {num2} = "))
        questions -= 1

        if user == product:
            correct += 1
            print(f"Correct | Qestions Left {questions}")
        else:
            incorrect += 1
            print(f"Incorrect | Questions Left {questions}")
    except ValueError:
        questions += 1
        print("Numbers Only")
