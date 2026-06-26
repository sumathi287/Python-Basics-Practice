# Accessing elements
# Adding Elements
list_var = [2, 3, 4, 6, 7]
list_var.append(90)
print(list_var)
# insert
list_var.insert(3, 73)
print(list_var)
# extend
list_var.extend([0, 11])
print(list_var)
# Updating Elements
list_var[0] = "a"
print(list_var)
# remove
list_var.remove("a")
print(list_var)
#pop
list_var.pop()
print(list_var)
#delete element
del list_var[0]
print(list_var)
