d = int(input("Enter the date as DD: "))
m = int(input("Enter the month as MM: "))
y = int(input("Enter the year as YYYY: "))

if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10:
    if d == 31:
        d = 1
        m += 1
        print(f"Next Date: {d}/{m}/{y}")
    else:
        d += 1
        print(f"Next Date: {d}/{m}/{y}")

elif m == 4 or m == 6 or m == 9 or m == 11:
    if d == 30:
        d = 1
        m += 1
        print(f"Next Date: {d}/{m}/{y}")
    else:
        d += 1
        print(f"Next Date: {d}/{m}/{y}")

elif m == 12:
    if d == 31:
        d = 1
        m = 1
        y += 1
        print(f"Next Date: {d}/{m}/{y}")
    else:
        d += 1
        print(f"Next Date: {d}/{m}/{y}")

elif m == 2:
    if y%400 == 0:
        if d == 29:
            d = 1
            m += 1
            print(f"Next Date: {d}/{m}/{y}")
        else:
            d += 1
            print(f"Next Date: {d}/{m}/{y}")
    elif y%100 == 0:
        if d == 28:
            d = 1
            m += 1
            print(f"Next Date: {d}/{m}/{y}")
        else:
            d += 1
            print(f"Next Date: {d}/{m}/{y}")
    elif y%4 == 0:
        if d == 29:
            d = 1
            m += 1
            print(f"Next Date: {d}/{m}/{y}")
        else:
            d += 1
            print(f"Next Date: {d}/{m}/{y}")
    else:
        if d == 28:
            d = 1
            m += 1
            print(f"Next Date: {d}/{m}/{y}")
        else:
            d += 1
            print(f"Next Date: {d}/{m}/{y}")