baby = 0
kid = 14
adult = 23
senior = 18
total = 0
count = 0

age = int(input("Enter the age: "))
while age != 0:
    if age <= 2:
        total += baby
    elif age <= 12:
        total += kid
    elif age <= 64:
        total += adult
    elif age >= 65:
        total += senior
    count += 1
    age = int(input("Enter the age: "))
print(f"Total Cost: ${format(total, '.2f')}")