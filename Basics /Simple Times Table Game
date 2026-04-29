from random import randint
questions = 10
correct = 0
wrong = 0

while True:
    if questions == 0:
        product = correct / 10 * 100
        print(f"You got {correct} / 10")
        print(f"Your percentage was {product}%")
        break
    num1 = randint(2,12)
    num2 = randint(2,12)
    product = (num1 * num2)
    answer = int(input(f"{num1} x {num2} = "))
    
    if product == answer:
        print(f"Correct | {questions - 1}")
        correct += 1
        questions -= 1

    else:
        print(f"Incorrect | {questions - 1}")
        wrong += 1
        questions -= 1
