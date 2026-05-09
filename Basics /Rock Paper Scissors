from random import choice
from time import sleep
count = 0
player_score = 0; computer_score = 0
while True:
    try:
        games = int(input("How many games would you like to play: "))

        if games == 0:
            print("You cant play 0 games")
            continue
        elif games >= 50:
             print("To many games");sleep(0.3)
             continue
        break
    except ValueError:
            print("Invaild choice");sleep(0.3)
print(f"You are going to play {games} games of rock paper scissors");sleep(1)
for x in range(games):
    count += 1
    options = ["rock", "paper", "scissors"]
    print(f"==== GAME {count} ====");sleep(1)
    user = input("Enter choice: Rock , Paper , Scissors\nEnter option: ").lower()
    while user not in options:user = input("\nEnter choice: Rock , Paper , Scissors\nEnter option: ").lower()
    print("\nLoading computer choice");sleep(1)
    computer_choice = choice(options)
    win = user == "paper" and computer_choice == "rock" or \
        user == "scissors" and computer_choice == "paper" or \
        user == "rock" and computer_choice == "scissors" \
        
    if win:
         print(f"\nWin Computer Output: {computer_choice}\n");sleep(0.5);player_score += 1
    elif user == computer_choice:
        print(f"\nDraw Computer Output: {computer_choice}\n");sleep(0.5);
    else:
        print(f"\nLose Computer Output: {computer_choice}\n");sleep(0.5);computer_score += 1

print(f"Your score: {player_score} | Computer score: {computer_score}")
