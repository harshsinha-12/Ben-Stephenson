m = float(input("Enter the mass of Water in grams: "))
t = float(input("Enter the temperature change in Celsius: "))
q = m * 4.186 * t
print(f"The energy needed to heat the water is {q} Joules.")
ep = 8.9
j_to_kwh = 2.777e-7 * q
cost = j_to_kwh * ep
print(f"The cost of boiling water is {cost} cents.")