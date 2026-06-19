student = {
    "name" : "Aditya",
    "age": 18,
    "city" : "Meerut",
    "Marks in Math" :  85,
    "Marks in Science" : 95,
    "Marks in English" : 96,
}

# print(student["name"])
# print(student["age"])
# print(student["Marks in Math"])
for key, value in student.items():
    print(f"{key}: {value}")