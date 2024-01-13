d = int(input("Enter birth date: "))    
m = input("Enter birth month: ")
if m == 'January':
    if d <= 19:
        print("Capricorn")
    else:
        print("Aquarius")
elif m == 'February':
    if d <= 18:
        print("Aquarius")
    else:
        print("Pisces")
elif m == 'March':
    if d <= 20:
        print("Pisces")
    else:
        print("Aries")
elif m == 'April':
    if d <= 19:
        print("Aries")
    else:
        print("Taurus")
elif m == 'May':
    if d <= 20:
        print("Taurus")
    else:
        print("Gemini")
elif m == 'June':
    if d <= 20:
        print("Gemini")
    else:
        print("Cancer")
elif m == 'July':
    if d <= 22:
        print("Cancer")
    else:
        print("Leo")
elif m == 'August':
    if d <= 22:
        print("Leo")
    else:
        print("Virgo")
elif m == 'September':
    if d <= 22:
        print("Virgo")
    else:
        print("Libra")
elif m == 'October':
    if d <= 22:
        print("Libra")
    else:
        print("Scorpio")
elif m == 'November':
    if d <= 21:
        print("Scorpio")
    else:
        print("Sagittarius")
elif m == 'December':
    if d <= 21:
        print("Sagittarius")
    else:
        print("Capricorn")
else:
    print("Invalid input.")