try:
    age = float(input("Enter your age: "))
    if age >= 18:
        print("Congrants 👏👏\nYou are eligible to vote!!")
    elif age < 18 and age >= 1:
        print("Sorry ☹️   !!\nYou are not eligible to vote!!")
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input!!")
