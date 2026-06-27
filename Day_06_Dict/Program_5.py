# Check whether a key exists.
student_info = {"name": "Alice", "age": 25, "department": "Physics"}
key = "age"
if key in student_info:
    print(f"The {key } key is exists in the dict")
else:
    print(f"The {key} key is not exists in the dict")
