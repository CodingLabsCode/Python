from random import choice as c
from time import time as t
question_one = """How Do You Call Upon A Function:
(1)def.greet()
(2)greet()
(3)greet
(4)say.greet()
Enter Answer: """

question_two = """How Do You Make a Function:
(1)func
(2)fn()
(3)def
(4)function
Enter Answer: """

question_three = """How Do You Make a List
(1)var = {}
(2)var = <>
(3)var = ()
(4)var = []
Enter Answer: """

question_four = """How Do You Import a Module / Libary
(1)import
(2)include
(3)bring
(4)user
Enter Answer: """

questions = [question_one, question_two, question_three, question_four]
answer_one = "2"
answer_two = "3"
answer_three = "4"
answer_four = "1"

correct = 0
incorrect = 0
AmountOfQuestions = 4
print("=== PYTHON QUIZ ===")
input("Press Enter To Begin: ")
start = t()
for i in range(4):
    AmountOfQuestions -= 1
    choice = c(questions)
    questions.remove(choice)
    if choice == question_one:
        user = input(choice)
        if user == answer_one:
            print(f"Correct | Questions Left {AmountOfQuestions}")
            correct += 1
        else:
            print(f"Incorrect | Questions Left {AmountOfQuestions}")
            incorrect += 1
    elif choice == question_two:
        user = input(choice)
        if user == answer_two:
            print(f"Correct | Questions Left {AmountOfQuestions}")
            correct += 1
        else:
            print(f"Incorrect | Questions Left {AmountOfQuestions}")
            incorrect += 1
    elif question_three:
        user = input(choice)
        if user == answer_three:
            print(f"Correct | Questions Left {AmountOfQuestions}")
            correct += 1
        else:
            print(f"Incorrect | Questions Left {AmountOfQuestions}")
            incorrect += 1
    elif question_four:
        user = input(choice)
        if user == answer_four:
            AmountOfQuestions -= 1
            print(f"Correct | Questions Left {AmountOfQuestions}")
            correct += 1
        else:
            AmountOfQuestions -= 1
            print(f"Incorrect | Questions Left {AmountOfQuestions}")
            incorrect += 1
end = t()
finished = f"""
Correct {correct}
Incorrect {incorrect}
Time Taken {end - start:.2f}"""

print(finished)
