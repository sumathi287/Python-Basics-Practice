try:
    first_number = float(input("Enter a 1st number: "))
    second_number = float(input("Enter a 2nd number: "))
    third_number = float(input("Enter a 3rd number: "))
    if (first_number >= second_number) and (first_number >= third_number):
        print(f"the {first_number} is larger one!!")
    elif (second_number >= first_number) and (second_number >= third_number):
        print(f"the {second_number} is larger one!!")
    else:
        print(f"the {third_number} is larger one!!")

except ValueError:
    print("Invalid input!!")
