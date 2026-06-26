# Find the largest number in a list.
var = [10, 30, 20, 55, 43]
list_length = len(var)
largest_number = var[0]
# The logic to rearrange the list elements in accending order
for i in range(list_length):
    if var[i] > largest_number:
        largest_number = var[i]
print(f"The largest number in the list is {largest_number}")
