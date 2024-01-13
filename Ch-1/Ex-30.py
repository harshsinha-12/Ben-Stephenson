kps = float(input("Enter the pressure in Kilo-pascals: "))
pounds_per_square_inch = kps * 0.145037738  
millimeters_of_mercury = kps * 7.50062
atmosphere = kps * 0.00986923
print(f"The pressure in pounds per square inch is {pounds_per_square_inch}.")
print(f"The pressure in millimeters of mercury is {millimeters_of_mercury}.")
print(f"The pressure in atmosphere is {atmosphere}.")
