m = input("Enter the name of Month: ")
if m == "February":
    print("No. of days: 28/29 days")
elif m in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif m in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 days")
else:
    print("Invalid input.")