from random import randint

def error(msg):
    print(f"[ERROR] {msg}")
def mul(x,y):
    return x * y

bouns_score = False
streak = 0
correct = 0
incorrect = 0
questions = 10
score = 0
beForQuestions = questions
count = 0
input("Click Enter When Ready")
while questions != 0:
    count += 1
    num1 = randint(2,12)
    num2 = randint(2,12)
    answer = mul(num1,num2)

    print(f"QUESTION {count}")

    try:
        user = int(input(f"{num1} x {num2} = "))
        questions -= 1
        if user == answer:
            correct += 1
            score += 2
            streak += 1
            print(f"Correct | Questions Left {questions}")
            if streak == 5 and bouns_score == False:
                score += 5
                bouns_score = True
        else:
            incorrect += 1
            score -= 1
            streak = 0
            print(f"Incorrect | Questions Left {questions}")
    except ValueError:
        error("Invaild Intger")
        questions += 1
        count -= 1
finshed = f"""Results
Correct {correct} / {beForQuestions}
Incorrect {incorrect} / {beForQuestions}
Score {score}
Streak {streak}"""

print(finshed)
