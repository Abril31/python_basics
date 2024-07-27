people = {
    "Bruno": "+591 72095120",
    "Carol": "+591 70597122",
    "Rick": "+591 75845133",
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Found {number}")
else:
    print("Not found")

# Another way 
# people = [
#     {"name": "Bruno", "number": "+591 72095120"},
#     {"name": "Carol", "number": "+591 70597122"},
#     {"name": "Rick", "number": "+591 75845133"},
# ]

# name = input("Name: ")
# for person in people:
#     if person["name"] == name:
#         #number = person["number"]
#         print(f"Found {person['number']}")
#         break
# else:
#     print("Not found")

# names = ["Bruno", "Niah", "Mimi"]

# name = input("Name: ")

# if name in names:
#     print("Found")
# else:
#     print("Not found")
