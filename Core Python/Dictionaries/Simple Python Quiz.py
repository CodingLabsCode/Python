from random import shuffle as s
from time import time as t

questions = [
    {"q": "How Do You Call A Function\n(1)greet()\n(2)def.greet\n(3)say.greet()\n Enter Answer: ", "a": "1"},
    {"q": "How Do You Make a Function\n(1)func\n(2)function\n(3)def\nEnter Answer: ", "a": "3"},
    {"q": "How Do You Make A List\n(1)var[]\n(2)var{}\n(3)var <>\nEnter Answer: ","a": "1"}
]
questionsLeft = len(questions)
s(questions)
correct = 0
incorrect = 0
streak = 0
score = 0
print("=== Python Quiz ===")
print("If you get a streak of 3 you get a score bonus of 4")
print("If you get an answer correct you gain 2 score but if you get an answer incorrect you lose 1 score")
input("Press Enter To Start")
start = t()

for item in questions:
    user = input(item["q"])
    questionsLeft -= 1
    if user == item["a"]:
        correct += 1
        streak += 1
        score += 2
        print(f"Correct You Have A Streak Of {streak} | Questions Left {questionsLeft}")
    else:
        incorrect += 1
        streak = 0
        score -= 1
        print(f"Incorrect You Have A Streak Of {streak} | Questions Left {questionsLeft}")
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
