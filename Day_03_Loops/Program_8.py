# Guess the number game.
import random

try:
    random_number = random.randint(1, 100)  # The range for select the random number
    count = 1
    number = int(input("Enter a number between 1 to 100 to compare: "))
    # Logic to compare and give the clue to find the random number until user found the random number choosen by computer
    while count != 0:
        if number == random_number:
            print("Correct!!")
            print(f"The random number is {random_number}")
            count = 0
        elif number > random_number:
            number = int(input("The number too high !!\nRe-enter the number: "))
        elif number < random_number:
            number = int(input("The number too low !!\nRe-enter the number: "))
except ValueError:
    print("Invalid input!!")
