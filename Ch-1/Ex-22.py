s1 = float(input("Enter the length of the first side of the triangle in centimeters: "))
s2 = float(input("Enter the length of the second side of the triangle in centimeters: "))
s3 = float(input("Enter the length of the third side of the triangle in centimeters: "))

semi = (s1 + s2 + s3) / 2
import math
area = math.sqrt(semi * (semi - s1) * (semi - s2) * (semi - s3))

print(f"The area of the triangle is {area} square centimeters.")