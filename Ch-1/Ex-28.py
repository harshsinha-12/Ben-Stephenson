at = float(input("Enter the air temperature in Celsius:"))
ws = float(input("Enter the wind speed in km/h:"))
wci = 13.12 + 0.6215*at - 11.37*ws**0.16 + 0.3965*at*ws**0.16
print(f"The wind chill index is {wci}.")