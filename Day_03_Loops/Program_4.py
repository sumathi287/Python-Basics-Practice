# Find the sum of numbers from 1 to N.
sum_of_numbers = 0
try:
    number = int(input("enter the number: "))
    number = number + 1
    for i in range(1, number):
        sum_of_numbers = sum_of_numbers + i
    print(f"the sum of the numbers from 1 to {number-1} is {sum_of_numbers}")
except ValueError:
    print("Invalid input!!")
