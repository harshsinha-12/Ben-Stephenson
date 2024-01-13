# f(x) = ax^2 + bx + c
import math
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"The roots are {x1} and {x2}.")
elif d == 0:
    x = -b / (2 * a)
    print(f"The root is {x}.")
else:
    print("The equation has no real roots.")