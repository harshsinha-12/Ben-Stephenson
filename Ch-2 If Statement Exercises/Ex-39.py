d = int(input("Enter the Sound Level in decibels: "))
if d < 40:
    print("The sound level is quiet.")
elif d == 40:
    print("The sound level is of a quite room.")
elif d < 70:
    print("The sound level is between a quite room and that of an alarm clock.")
elif d == 70:
    print("The sound level is of an alarm clock.")
elif d < 106:
    print("The sound level is between an alarm clock and a gas lawnmower.")
elif d == 106:
    print("The sound level is of a gas lawnmower.")
elif d < 130:
    print("The sound level is between a gas lawnmower and a jackhammer.")
elif d == 130:
    print("The sound level is of a jackhammer.")
else:
    print("The sound level is greater than that of a jackhammer.")