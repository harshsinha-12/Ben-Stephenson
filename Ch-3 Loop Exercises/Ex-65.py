p = 0
for i in range(1,6):
    x = float(input(f"Enter the X coordinate of side {i}: "))
    y = float(input(f"Enter the Y coordinate of side {i}: "))
    d = ((x**2)+(y**2))**0.5
    p = p + d
print(f"Perimeter of the pentagon is: {p}")
