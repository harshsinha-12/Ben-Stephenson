print("Temperature in Celcius\tTemperature in Fahrenheit")

for i in range(0, 101, 10):
    print(f"{i} C \t\t\t\t\t {format((i*9/5)+32, '.2f')} F")