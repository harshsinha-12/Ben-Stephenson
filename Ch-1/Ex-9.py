p = float(input("Enter the principal amount: "))
i = 0.04
t1,t2,t3 = 1,2,3
a1 = p * (1+i)**t1
a2 = p * (1+i)**t2
a3 = p * (1+i)**t3
print(f"The amount after {t1} years is {format(a1, '.2f')}.")
print(f"The amount after {t2} years is {format(a2, '.2f')}.")
print(f"The amount after {t3} years is {format(a3, '.2f')}.")