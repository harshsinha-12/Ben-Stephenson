y = int(input("Enter the year: "))

if y%400 == 0:
    print(f"{y} is a leap year.")
elif y%100 == 0:
    print(f"{y} is not a leap year.")
elif y%4 == 0:
    print(f"{y} is a leap year.")
else:
    print(f"{y} is not a leap year.")
