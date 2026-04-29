import time

player_stats = {
    "Name": "Billy Bob",
    "Level": 15,
    "Class": "Wizzard",
    "Health": 100
}

print("STATS")
print("-----")
print("Name:", player_stats["Name"])
print("Level:", player_stats["Level"])
print("Health", player_stats["Health"])
print("Class:", player_stats["Class"])
print("-----")
user_input = input("Would you like to enter a boss fight (yes / no)").lower()
if user_input == "yes":
    print("You enter a boss fight")

    player_stats["Level"] = 18
    player_stats["Health"] = 55

    print("Loading...")
    time.sleep(1)
    print("Boss Fight Ending")
    time.sleep(2)
    print("Boss Fight Ended")
 
    print("Stats after boss fighr ")

    print("STATS")
    print("-----")
    print("Name:", player_stats["Name"])
    print("Level:", player_stats["Level"])
    print("Health", player_stats["Health"])
    print("Class:", player_stats["Class"])
    print("-----")
    print("Your went up 3 Levels well done ")

elif  user_input == "no":
    print("You enter the forest instead of fighting the boss")
    time.sleep(1)
    print("You come across a wold trying to eat you")
    user_input = input("Do you fight the wolf or run away (fight / run away)")

    if user_input == "fight":
        print("You slay the wolf and level up")
        print("Level incressed by 2 ")
        print("Your health went down by 10")
        player_stats ["Health"] = 45
        player_stats ["Level"] = 20
        print("you drank a health potion, your health raised to 100")
        print("STATS")
        print("-----")
        print("Name:", player_stats["Name"])
        print("Level:", player_stats["Level"])
        print("Class:", player_stats["Class"])
        print("-----")
