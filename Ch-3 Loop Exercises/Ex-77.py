import math

a = input("Enter the number in binary: ")
num = 0
for i in range(len(a)):
    num += int(a[-i-1]) * int(math.pow(2, i))
print(num)
