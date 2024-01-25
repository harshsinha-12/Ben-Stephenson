x = float(input("Enter the number: "))
guess = x / 2
c = 0
while abs(guess * guess - x) > 10**(-12):
    c += 1
    guess = (guess + x / guess) / 2
print("Good Guess after ", c, " iterations")