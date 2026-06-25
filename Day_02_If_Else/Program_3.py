try:
    number_1 = input("Enter the 1st number to compare: ")
    number_2 = input("Enter the 2nd number to compare: ")
    number_1 = float(number_1)
    number_2 = float(number_2)
    if number_1 > number_2:
        print(f"the {number_1} is largest number!!")
    elif number_1 < number_2:
        print(f"the {number_2} is largest number!!")
    else:
        print("Both numbers are equal!!")
except ValueError:
    print("Invalid input")
