n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
MAX = max(n1, n2, n3)
MIN = min(n1, n2, n3)
MID = (n1 + n2 + n3) - MAX - MIN
print(f"The numbers in ascending order are {MIN}, {MID} and {MAX}.")