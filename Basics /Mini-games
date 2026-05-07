from random import randint
from random import choice
from time import sleep

def tts():
    user_questions = int(input("\nHow many qestions would you like\n"))
    print("Loading questions\n")
    sleep(0.5)

    questions = user_questions
    incorrect = 0 
    correct = 0
    orgianl_questions = questions
    try:
        while True:
            if questions == 0:
                print(f"You got {correct}/ {orgianl_questions}")
                sleep(0.3)
                lobby()
                break
                    
            num1 = randint(2,12)
            num2 = randint(2,12)
            answer = num1 * num2
            sleep(0.2)
            input_user = int(input(f"{num1} x {num2} ="))

            if input_user == answer:
                correct += 1
                questions -= 1 
                print(f"Correct | Questions left {questions}")
                sleep(0.2)
            else:
                incorrect += 1
                questions -= 1
                print(f"Incorrect | Questions left {questions}")
                sleep(0.2)
    except ValueError:
            print("Enter a number")

def rps():
    options = ["paper", "rock", "scissors"]
    player_score = 0
    computer_score = 0

    while player_score< 3 and computer_score < 3:
            user_choice = input("\nEnter a option Rock Paper or Scissors\n").lower()
            print("\nLoading Computer choice")
            sleep(0.5)
            computer_choice = choice(options)

            win = user_choice == "rock" and computer_choice == "scissors" or \
                user_choice == "paper" and computer_choice == "rock" or \
                user_choice == "scissors" and computer_choice == "paper" \
                
            if win:
                print(f"\nYou won this round Your choice: {user_choice} | Computer choice: {computer_choice}\n")
                player_score += 1
            elif user_choice == computer_choice:
                print(f"\nDraw no one got a point Your choice: {user_choice} | Computer choice: {computer_choice}\n")
            else:
                computer_score += 1
                print(f"\nComputer won this round Your choice: {user_choice} | Computer choice: {computer_choice}\n")
        
    if player_score == 3:
        print(f"You won well done Your points: {player_score} | Computer points: {computer_score}\n")
        sleep(0.3)
        lobby()
    else:
        print(f"Computer won Computer points: {player_score} | Your points: {player_score}\n")
        sleep(0.3)
        lobby()


def numberguess():
    number = randint(1,6)
    guess = int(input("Guess a number between 1, 10:\n"))

    while guess != number:
        guess = int(input("Try Again\n"))

        if guess < number:
            print("To Low:\n")
        elif guess > number:
            print("To High:\n")

    if guess == number:
        print("You got it right well done")
        sleep(0.3)
        lobby()

def lobby():
        global user_input
        user_input = input("==== Mini Games ====\n---- Select A Game ----\n1()Rock Paper Scissors\n2()Times Tables\n3()Number Guessing\n==== More Coming Soon ====\nEnter Option: ")
        sleep(0.4)
        match user_input:
            case "1":
                rps()
            case "2":
                tts()
            case "3":
                numberguess()
lobby()
