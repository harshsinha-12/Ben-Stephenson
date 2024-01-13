import math

n = int(input("Enter numner of sides of polygon: "))    
s = float(input("Enter the length of each side: "))

area = (n * s**2) / (4 * math.tan(math.pi/n))

print(f"The area of the polygon is {area} square units.")
