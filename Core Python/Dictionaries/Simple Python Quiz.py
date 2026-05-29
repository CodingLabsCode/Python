from random import shuffle 
from time import time 
Bonus_score = False
questions = [
    {"q": "How Do You Make A List\n(1)var = {}\n(2)var = ()\n(3)var = []\n(4)var = <>\nEnter Answer: ", "a": "3"},
    {"q": "How Do You Call Upon A Function\n(1)greet()\n(2)def.greet\n(3)say.greet()\n(4)bring.greet()\nEnter Answer: ", "a": "1"},
    {"q": "How Do You Make A Function\n(1)func\n(2)def\n(3)function\n(4)fn()\nEnter Answer: ", "a": "2"},
    {"q": "How Do You Import A Module / Library (e.g random , time ect)\n(1)bring\n(2)include\n(3)user\n(4)import\nEnter Answer:", "a": "4" },
    {"q": "Which One Prints Stuff To The Screen\n(1)echo()\n(2)print\n(3)say\n(4)show\nEnter Answer: ", "a": "2"},
    {"q": "What Data Type Is /Hello/\n(1)string\n(2)float\n(3)integer\n(4)boonlean\nEnter Answer: ", "a": "1"}
]
shuffle(questions)

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
start = time()
for i, item in enumerate(questions, start=1):
    print(f"Question {i} | Questions Left {questionsLeft}\n")
    user = input(item["q"])
    print("\n", end="")
    questionsLeft -= 1
    if user == item["a"]:
        correct += 1
        score += 2
        streak += 1
        if streak >=3 and Bonus_score == False: 
            score += 4 
            Bonus_score = True
            print("Bonus Score Of 4 Added")
        print(f"Correct | Streak {streak}")
    else:
        incorrect += 1
        score -= 1
        streak = 0
        print(f"Incorrect | Streak {streak}\n")
    if score <= -1: score = 0
end = time()
time_taken = end - start
print("You Got An Insane Time" if time_taken <=20 else "You Got A Good Time" )
finshed = f"""=== Results ===
Correct {correct} / {amoutOfQuestions}
Incorrect {incorrect} / {amoutOfQuestions}
Streak {streak}
Score {score}
Time Taken {end - start:.2f}"""
print(finshed)
