from random import shuffle as s
from time import time as t

questions = [
    {"q": "How Do You Make A List\n(1)var = {}\n(2)var = ()\n(3)var = []\n(4)var = <>\nEnter Answer: ", "a": "3"},
    {"q": "How Do You Call Upon A Function\n(1)greet()\n(2)def.greet\n(3)say.greet()\n(4)bring.greet()\nEnter Answer: ", "a": "1"},
    {"q": "How Do You Make A Function\n(1)func\n(2)def\n(3)function\n(4)fn()\nEnter Answer: ", "a": "2"},
    {"q": "How Do You Import A Module / Library (e.g random , time ect)\n(1)bring\n(2)include\n(3)user\n(4)import\nEnter Answer:", "a": "4" },
    {"q": "Which One Prints Stuff To The Screen\n(1)echo()\n(2)print\n(3)say\n(4)show\nEnter Answer: ", "a": "2"},
    {"q": "What Data Type Is /Hello/\n(1)string\n(2)float\n(3)integer\n(4)boonlean", "a": "1"}
]
s(questions)

questionsLeft = len(questions)
amoutOfQuestions = len(questions)
correct = 0
incorrect = 0
score = 0
streak = 0

print("=== Python Quiz ===")
print("If You Get A Streak Of 3 You Get A Score Bonus Of 4")
print("You Get 2 Score For Each Qestion You Get Correct BUT For Eacb Questions You Get Incorrect You Lose 1 Score")
input("Press Enter To Begin: ")
start = t()
for item in questions:
    user = input(item["q"])
    questionsLeft -= 1
    if user == item["a"]:
        correct += 1
        score += 2
        streak += 1
        print(f"Correct You Are On A Streak Of {streak} | Questions Left {questionsLeft}")
    else:
        incorrect += 1
        score -= 1
        streak = 0
        print(f"Incorrect You Are On A Streak Of {streak} | Questions Left {questionsLeft}")
    if score <= -1: score = 0
end = t()
time_taken = end - start
print("You Got An Insane Time" if time_taken <=20 else "You Got A Good Time" )
if streak >=3: score += 4 ;print("Bonus Score Of 4 Added")
finshed = f"""=== Results ===
Correct {correct} / {amoutOfQuestions}
Incorrect {incorrect} / {amoutOfQuestions}
Streak {streak}
Score {score}
Time Taken {end - start:.2f}"""
print(finshed)
