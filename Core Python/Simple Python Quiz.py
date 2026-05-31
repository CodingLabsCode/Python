from random import shuffle 
from time import time , sleep
from pathlib import Path

highscoreScore = Path("Score High Score.txt")
highscoreStreak = Path("Streak HighScore")

Bonus_score = False

questions = [
    {"q": "How Do You Make A List\n(1)var = {}\n(2)var = ()\n(3)var = []\n(4)var = <>\nEnter Answer: ", "a": "3"},
    {"q": "How Do You Call Upon A Function\n(1)greet()\n(2)def.greet\n(3)say.greet()\n(4)bring.greet()\nEnter Answer: ", "a": "1"},
    {"q": "How Do You Make A Function\n(1)func\n(2)def\n(3)function\n(4)fn()\nEnter Answer: ", "a": "2"},
    {"q": "How Do You Import A Module / Library (e.g random , time ect)\n(1)bring\n(2)include\n(3)user\n(4)import\nEnter Answer:", "a": "4" },
    {"q": "Which One Prints Stuff To The Screen\n(1)echo()\n(2)print\n(3)say\n(4)show\nEnter Answer: ", "a": "2"},
    {"q": "What Data Type Is /Hello/\n(1)string\n(2)float\n(3)integer\n(4)boolean\nEnter Answer: ", "a": "1"}
]
shuffle(questions)

questionsLeft = len(questions)
amountOfQuestions = len(questions)
correct = 0
incorrect = 0
score = 0
streak = 0

print("=== Python Quiz ===")
print("If You Get A Streak Of 4 You Get A Score Bonus Of 5")
print("You Get 2 Score For Each Question You Get Correct BUT For Each Questions You Get Incorrect You Lose 1 Score")
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
        if streak >=4 and Bonus_score == False: 
            score += 5 
            Bonus_score = True
        print(f"Correct | Streak {streak}")
    else:
        incorrect += 1
        score -= 1
        streak = 0
        print(f"Incorrect | Streak {streak}\n")
    if score <= -1: score = 0
end = time()
time_taken = end - start
finshed = f"""=== Results ===
Correct {correct} / {amountOfQuestions}
Incorrect {incorrect} / {amountOfQuestions}
Streak {streak}
Score {score}
Time Taken {end - start:.2f}
"""
print("You Got An Insane Time" if time_taken <=20 and correct >=3 else "You Got A Good Time" )
print("You Got A Bonus Score Of 5 Added" if Bonus_score == True else "You Did Not Get A Bonus Score")
print(finshed);sleep(5)
highscore_streak = []
highscore_score = []

highscore_score.append(score)
highscore_streak.append(streak)

highscoreStreak.write_text(f"{str(streak)}")
highscoreScore.write_text(f"{str(score)}\n")

sorted_score = sorted(highscore_score,reverse= True)
sorted_streak_score = sorted(highscore_streak, reverse=True)

def streakscore():
    for i, line in enumerate(sorted_streak_score, start=1):
        print(f"{i}: {line}")
def scoreScore():
     for i, line in enumerate(sorted_score, start=1):
        print(f"{i}: {line}")
while True:
    see_stats = input("=== STATS ===\n(1)Score Highscores\n(2)Streak HighScore\n(3)Exit\nEnter Choice: ")
    match see_stats:
        case "1":
            scoreScore()
        case "2":
            streakscore()
        case "3":
            print("GoodBye")
            exit()
