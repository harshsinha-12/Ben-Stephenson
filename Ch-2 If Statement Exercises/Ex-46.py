m = input("Enter the name of Month: ")
d = int(input("Enter the date: "))
if m == 'January' or m == 'February':
    print("Winter")
elif m == 'March':
    if d >= 20:
        print("Spring")
    else:
        print("Winter")
if m == 'April' or m == 'May':
    print("Spring")
elif m == 'June':
    if d >= 21:
        print("Summer")
    else:
        print("Spring")
if m == 'July' or m == 'August':
    print("Summer")
elif m == 'September':
    if d >= 22:
        print("Fall")
    else:
        print("Summer")
if m == 'October' or m == 'November':
    print("Fall")
elif m == 'December':
    if d >= 21:
        print("Winter")
    else:
        print("Fall")
        