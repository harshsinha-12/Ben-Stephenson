r = float(input("Enter the rating of employee: "))  

if r == 0:
    print("Unacceptable performance")
    raise_amount = 2400 * r
    print("Amount of raise: $", raise_amount)

elif r == 0.4:
    print("Acceptable performance")
    raise_amount = 2400 * r
    print("Amount of raise: $", raise_amount)

elif r >= 0.6:
    print("Meritorious performance")
    raise_amount = 2400 * r
    print("Amount of raise: $", raise_amount)
    
else:
    print("Invalid rating")
