f = float(input("Enter the frequency in hertz: "))  
if f > 260.63 and f < 262.3:
    print("The frequency is C4.")
elif f > 292.66 and f < 294.66:
    print("The frequency is D4.")
elif f > 328.63 and f < 330.63:
    print("The frequency is E4.")
elif f > 348.23 and f < 350.23:
    print("The frequency is F4.")
elif f > 391.00 and f < 393.00:
    print("The frequency is G4.")
elif f > 439.00 and f < 441.00:
    print("The frequency is A4.")
elif f > 492.88 and f < 494.88:
    print("The frequency is B4.")
else:
    print("The frequency is not in the range of the chromatic scale.")