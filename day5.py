# with open("test.txt", "r") as file:
#     # file.write("\nLine 2 from Aditya!")
#     # file.write("\nLine 3 - file handling is cool!")
#     content = file.read()
#     print(content)

import json

data = {"name": "Aditya", "age": 18, "city": "Meerut"}

#Save dictionary to file
with open("data.json", "w") as file:
    json.dump(data, file)

#Read dictionary back from file
with open("data.json", "r") as file:
    loaded = json.load(file)
    print(loaded)
    print(loaded["name"])