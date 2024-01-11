# 1.6km = 1 mile
# 1km = 0.621371 mile
# 1 gallon = 3.78541L
# 1L = 0.264172 gallon
m = float(input("Enter the distance in miles: "))
g = float(input("Enter the fuel amount in gallons: "))
mpg = m / g
gpm = g / m
lkm = ((gpm * 3.78541)/1.60934)*100
print(f"The fuel efficiency in miles per gallon is {mpg}.")
print(f"The fuel efficiency in liters per 100 kilometers is {lkm}.")