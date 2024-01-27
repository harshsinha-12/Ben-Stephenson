n = int(input("Enter the number: "))
f = 2
if n < 2:
    print("Invalid Input")
while f <= n:
    if n % f == 0:
        print(f"{f} is a prime factor")
        n = n//f
    else:
        f = f + 1

