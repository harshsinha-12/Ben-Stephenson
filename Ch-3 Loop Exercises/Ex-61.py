n = int(input("Enter the number: "))
total = 0
count = 0

while n != 0:
    total += n
    count += 1
    n = int(input("Enter the number: "))

average = total / count
print("Average is:", average)