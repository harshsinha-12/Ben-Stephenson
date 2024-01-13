n = int(input("Enter human years: "))
if n < 0:
    print("Invalid input.")
elif n <= 2:
    print(f"The dog years is {n*10.5}.")
else:
    print(f"The dog years is {21+(n-2)*4}.")
    