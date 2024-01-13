r = float(input("Enter the radius of cylinder in centimeters: "))
h = float(input("Enter the height of cylinder in centimeters: "))
import math
volume = math.pi * r ** 2 * h
print(f"The volume of the cylinder is {format(volume, '.1f')} cubic centimeters.")