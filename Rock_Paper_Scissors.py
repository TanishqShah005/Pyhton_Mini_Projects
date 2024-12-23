import random

print("Rock-Paper-Scissors Game")

while True:
    play = int(input("\n1. Play\n2. Exit\nChoose an option: "))

    if play == 1:
        user_choice = input("Rock, Paper, Scissors?\nEnter your choice: ").capitalize()

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid Input. Please choose Rock, Paper, or Scissors.")
            continue

        print()

        print("Your choice:", user_choice)
        print("Computer choice:", computer_choice)

        if user_choice == computer_choice:
            print("It's a Draw!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                (user_choice == "Paper" and computer_choice == "Rock") or \
                (user_choice == "Scissors" and computer_choice == "Paper"):
            print("You Win!")
        else:
            print("Computer Wins!")

        print("\n----- GAME OVER -----\n")

    elif play == 2:
        print("Thanks for playing. Goodbye!")
        break

    else:
        print("Invalid Input. Please choose 1 to Play or 2 to Exit.")
