n = 0.05
pennies = 5

t = 0.0
l = float(input("Enter the price of each item: "))
while l != 0:
    t += float(l)
    l = float(input("Enter the price of each item: "))
print(f"Total price is: {format(t, '.2f')}")

r = t * 100 % pennies
if r < pennies/2:
    t = t * 100 - r
else:
    t = t * 100 - r + pennies
print(f"Total price in pennies is: {t}")