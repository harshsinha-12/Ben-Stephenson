h = float(input("Enter the height in centimeters: "))
m = h/100
w = float(input("Enter the weight in kilograms: "))
bmi = w/(m**2)
print(f"The BMI is {bmi} kg/m^2.")