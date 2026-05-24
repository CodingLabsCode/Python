from random import choice as c
from time import time as t

print("If You answer 3  questions in a row correctly you get a score bonus of 4")
print("If you get an answer correct you gain 2 score but if you get an answer incorrect you lose 1 score")

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

question_five = """Which One Prints Stuff To The Screen
(1)echo()
(2)print()
(3)say()
(4)show
Enter Answer: """

question_six = """What Data Type is ("Hello")(with out the brackets)
(1)float
(2)integer
(3)boonlean
(4)string"""
questions = [question_one, question_two, question_three, 
             question_four, question_five, question_six]
answer_one = "2"
answer_two = "3"
answer_three = "4"
answer_four = "1"
answer_five = "2"
answer_six = "4"

correct = 0
incorrect = 0
streak = 0
score = 0
AmountOfQuestions = len(questions)
print("=== PYTHON QUIZ ===")
input("Press Enter To Begin: ")
start = t()
for i in range(len(questions)):
    AmountOfQuestions -= 1
    choice = c(questions)
    questions.remove(choice)
    if choice == question_one:
        user = input(choice)
        if user == answer_one:
            streak += 2
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
    elif choice == question_two:
        user = input(choice)
        if user == answer_two:
            streak += 2
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
    elif choice == question_three:
        user = input(choice)
        if user == answer_three:
            streak += 1
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
    elif choice == question_four:
        user = input(choice)
        if user == answer_four:
            streak += 1
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
    elif choice == question_five:
        user = input(choice)
        if user == answer_five:
            streak += 1
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
    elif choice == question_six:
        user = input(choice)
        if user == answer_six:
            streak += 1
            print(f"Correct You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            correct += 1
            score += 2
        else:
            streak = 0
            print(f"Incorrect You Are On A Streak Off {streak} | Questions Left {AmountOfQuestions}")
            incorrect += 1
            score -= 1
end = t()
timeTaken = end - start
if score <= -1: score = 0
if streak >=3: score += 4 ;print("Bonus Score Of 4 Added")
print("You Got A Good Streak" if streak >= 2 else "You Got Alright Streak")
print("You Got An Insane Time" if timeTaken <=10.00 else "You Got A Good Time" ) 
finished = f"""
Correct {correct}
Incorrect {incorrect}
Streak {streak}
Score {score}
Time Taken {end - start:.2f}"""

print(finished)
