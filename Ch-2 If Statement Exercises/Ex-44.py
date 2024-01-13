d = int(input("Enter the date: "))
m = input("Enter the month: ")
if m == 'January' and d == 1:
    print("New Year's Day")
elif m == 'July' and d == 1:
    print("Canada Day")
elif m == 'December' and d == 25:
    print("Christmas Day")
else:
    print("No holiday.")
