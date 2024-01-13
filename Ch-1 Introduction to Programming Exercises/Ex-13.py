cents_per_nickel = 5
cents_per_dime = 10
cents_per_quarter = 25
cents_per_loonie = 100
cents_per_toonie = 200

cents = int(input("Enter the number of cents: "))
toonies = cents // cents_per_toonie
cents = cents % cents_per_toonie

loonies = cents // cents_per_loonie
cents = cents % cents_per_loonie

quarter = cents // cents_per_quarter
cents = cents % cents_per_quarter

dimes = cents // cents_per_dime
cents = cents % cents_per_dime

nickels = cents // cents_per_nickel
cents = cents % cents_per_nickel

print(f"{toonies} toonies, {loonies} loonies, {quarter} quarters, {dimes} dimes, {nickels} nickels, {cents} cents.")
