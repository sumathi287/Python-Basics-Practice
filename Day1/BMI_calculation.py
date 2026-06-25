import sys
try:
    weight = input("Enter your weight: ")
    weight = int(weight)
    height = input("Enter your height in cm: ")
    height = int(height)
    height = height*0.01
except ValueError:
    print("Entered invalid input data\nEnd the program!")
    sys.exit()
BMI_var = (weight/(height * height))
print(f"your BMI calculation is {BMI_var}")