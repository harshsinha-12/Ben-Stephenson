a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


sum = a + b
diff = a - b
prod = a * b
quot = a // b
rem = a % b
expo = a ** b

import math
log = math.log10(a)

print(f"The sum of {a} and {b} is {sum}.")
print(f"The difference between {a} and {b} is {diff}.")
print(f"The product of {a} and {b} is {prod}.")
print(f"The quotient when {a} is divided by {b} is {quot}.")
print(f"The remainder when {a} is divided by {b} is {rem}.")
print(f"The result of {a} raised to the power of {b} is {expo}.")
print(f"The log of {a} is {log}.")
