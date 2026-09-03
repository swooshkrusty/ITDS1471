import random


# Q1
name = random.choice(["Meera", "Ben", "John", "Anand"])
score = random.randint(0, 100)

if score >= 70:
    print(f"{name} performed really well in the test and got a score of {score}")
elif score >= 50:
    print(f"{name} passed the test and got a score of {score}")
else:
    print(f"{name} failed the test with a score of {score}")


# Q2: Return "Ford"
lst = [1, 2, {"car": "Ford"}, "Hello"]

car = lst[2]["car"]
print(car)


# Q3: Return [2, 3, 4] using slicing
lst = [1, 2, 3, (1, 2, [1, 2, 3, 4, 5], 3, 2, 1, [1, 2])]

result = lst[3][2][1:4]
print(result)


# Q4: Extract the last three characters
codes = ["826GBR", "840USA", "276DEU", "818EGY", "250FRA"]

countries = [code[-3:] for code in codes]
print(countries)


# Q5: Return all names in uppercase
names = ["Sophie", "Mark", "Susan", "Jerome", "Roger", "Sunita", "Boris", "Steve"]

uppercase_names = [name.upper() for name in names]
print(uppercase_names)


# Q6: Keep only integers
Lst = [1, 2, 3, 4, "Helena", 9, 2.8724, 4, 2, "Rick", {"name": "John"}]

integers = [item for item in Lst if isinstance(item, int)]
print(integers)


# Q7
def process_data(value):
    if isinstance(value, list):
        return sorted(value)
    elif isinstance(value, tuple):
        return len(value)
    elif isinstance(value, str):
        return value.upper()
    else:
        print("This is not a string, tuple or list")


# Q8
def contains_number(text):
    return any(character.isdigit() for character in text)


# Q9: Keep only people whose favorite color is Blue
person = [
    ("Andrew", 39, "Blue"),
    ("Ross", 48, "Red"),
    ("Sarah", 19, "Yellow"),
    ("Meena", 42, "Orange"),
    ("Sophue", 28, "Blue"),
]

blue_people = [individual for individual in person if individual[2] == "Blue"]
print(blue_people)