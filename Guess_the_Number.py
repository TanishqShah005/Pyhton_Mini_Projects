import random

target = random.randint(1, 100)
count = 0

while True:
    userChoice = input("Guess the Number or Quit (Q): ")
    if userChoice.lower() == "q":
        break

    try:
        userChoice = int(userChoice)
        if userChoice == target:
            count += 1
            print("Correct Guess !!!, You are a Genius !!!")
            print("No. of Guesses:", count)
            break

        elif userChoice < target:
            count += 1
            print("Your Guess is Smaller, take a Bigger Guess ...")
        else:
            count += 1
            print("Your Guess is Bigger, take a Smaller Guess ...")

    except ValueError:
        print("Invalid input! Please enter a number or 'Q' to quit.")

print("----- GAME OVER -----")
