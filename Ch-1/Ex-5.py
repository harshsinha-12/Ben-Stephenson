c_small = int(input("Enter the number of containers holding less than 1L: "))
c_big = int(input("Enter the number of containers holding 1L or more: "))
refund = c_small * 0.10 + c_big * 0.25
print(f"The total refund is ${refund}.")