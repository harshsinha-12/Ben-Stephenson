p = float(input("Enter the pressure of the gas in pascals: "))
v = float(input("Enter the volume of the gas in liters: "))
t = float(input("Enter the temperature of the gas in kelvin: "))

# n = pv/8.314t

n = (p * v) / (8.314 * t)
print(f"The number of moles of gas is {n} moles.")
