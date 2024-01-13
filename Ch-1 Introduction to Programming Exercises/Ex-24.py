d = int(input("Enter the number of days: "))
h = int(input("Enter the number of hours: "))
m = int(input("Enter the number of minutes: "))
s = int(input("Enter the number of seconds: "))

total_seconds = d*24*60*60 + h*60*60 + m*60 + s

print(f"The total number of seconds is {total_seconds} seconds.")