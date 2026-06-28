# creating a set
var_set = {"Alice", "Perry", 44, (23, 34), 44}
print(var_set)
# adding elements
var_set.add("apple")
print(var_set)
# remove element
var_set.remove("Alice")
print(var_set)
# Checking existence using in
if "apple" in var_set:
    print("yes")
# Length of set
length_set = len(var_set)
print(length_set)
# union
var_set2 = {10, 20, 30, 40}
var_set3 = {50, 60, 70, 80, 40}
var_set4 = var_set2.union(var_set3)
print(var_set4)
var_set4 = var_set2.intersection(var_set3)
print(var_set4)
var_set4 = var_set2.difference(var_set3)
print(var_set4)
