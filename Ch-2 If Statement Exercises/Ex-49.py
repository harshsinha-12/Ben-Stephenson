m = float(input("Enter the magnitude of the earthquake: "))
if m < 2.0:
    print("It is a micro earthquake.")
elif m >= 2.0 and m < 3.0:
    print("It is a very minor earthquake.")
elif m >= 3.0 and m < 4.0:
    print("It is a minor earthquake.")
elif m >= 4.0 and m < 5.0:
    print("It is a light earthquake.")
elif m >= 5.0 and m < 6.0:
    print("It is a moderate earthquake.")
elif m >= 6.0 and m < 7.0:
    print("It is a strong earthquake.")
elif m >= 7.0 and m < 8.0:
    print("It is a major earthquake.")
elif m >= 8.0 and m < 10.0:
    print("It is a great earthquake.")
else:
    print("It is a meteoric earthquake.")
    