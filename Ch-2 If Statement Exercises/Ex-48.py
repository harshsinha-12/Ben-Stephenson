y = int(input("Enter the year: "))
dragon = (y - 2000) % 12
if dragon == 0:
    print("Dragon")
elif dragon == 1:
    print("Snake")
elif dragon == 2:
    print("Horse")
elif dragon == 3:
    print("Sheep")
elif dragon == 4:
    print("Monkey")
elif dragon == 5:
    print("Rooster")
elif dragon == 6:
    print("Dog")
elif dragon == 7:
    print("Pig")
elif dragon == 8:
    print("Rat")
elif dragon == 9:
    print("Ox")
elif dragon == 10:
    print("Tiger")
elif dragon == 11:
    print("Hare")
else:
    print("Invalid input.")