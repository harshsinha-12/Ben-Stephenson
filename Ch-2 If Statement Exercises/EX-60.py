from random import randrange

n = randrange(0, 38)
if n == 37:
    print("The spin resulted in 00...")
else:
    print("The spin resulted in ...", n)

if n == 37:
    print("Pay 00")
else:
    print("Pay", n)

if n ==37:
    print("Pay 00")
elif n == 0:
    print("Pay 0")

# red = 1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36
# black = 2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35
    
if n < 10 and n % 2 == 1:
    print("Pay Red")
elif n < 19 and n % 2 == 0:
    print("Pay Red")
elif n < 28 and n % 2 == 1:
    print("Pay  Red")
elif n < 37 and n % 2 == 0:
    print("Pay Red")
else:
    print("Pay Black")


if n % 2 == 0:
    print("Pay Even")
else:
    print("Pay Odd")
if n < 19:
    print("Pay 1 to 18")
else:
    print("Pay 19 to 36")