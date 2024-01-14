f = float(input("Enter the Frequency in Hz: "))
if f < 3e9:
    print("Radio Waves")
elif f < 3e12:
    print("Microwaves")
elif f < 4.3e14:
    print("Infrared Light")
elif f < 7.5e14:
    print("Visible Light")
elif f < 3e17:
    print("Ultraviolet Light")
elif f < 3e19:
    print("X-Rays")
else:
    print("Gamma Rays")
    