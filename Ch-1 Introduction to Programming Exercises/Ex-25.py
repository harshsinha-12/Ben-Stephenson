s = int(input("Enter the number of seconds: ")) 

d = s // (24 * 60 * 60)
s = s % (24 * 60 * 60) 

h = s // (60 * 60)
s = s % (60 * 60)

m = s // 60
s = s % 60

print(f"The total number of days is {d} days, {h} hours, {m} minutes and {s} seconds.")