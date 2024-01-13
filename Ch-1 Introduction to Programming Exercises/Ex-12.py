import math

t1 = float(input("Enter Latitude 1: "))
g1 = float(input("Enter Longitude 1: "))
t2 = float(input("Enter Latitude 2: "))
g2 = float(input("Enter Longitude 2: "))

distance = 6371.01 * math.acos(math.sin(math.radians(t1))
                                * math.sin(math.radians(t2)) 
                                + math.cos(math.radians(t1)) 
                                * math.cos(math.radians(t2)) 
                                * math.cos(math.radians(g1 - g2)))
print(f"The distance between the two points is {distance} km.")