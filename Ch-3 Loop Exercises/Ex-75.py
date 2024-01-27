a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
if a > b:
    d = b
else:
    d = a
while d > 0:
    if a % d == 0 and b % d == 0:
        print("HCF of", a, "and", b, "is", d)
        break
    d -= 1

