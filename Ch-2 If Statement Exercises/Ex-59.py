#AAA333
#4444AAA

a = input("Enter the string in numberplate: ")
i = int(input("Enter the digits in numberplate: "))

f = str(i) + a

if len(str(i)) == 3 and (len(a) == 3 and a.isalpha()):
    if a == a.upper() and type(i) is int :
        print("The numberplate is valid and is of old style.")
    else:
        print("The numberplate is invalid.")


elif len(str(i)) == 4 and (len(a) == 3 and a.isalpha()):
    if a == a.upper() and type(i) is int:
        if f[4:7].isalpha():
            print("The numberplate is valid and is of new style.")
    else:
        print("The numberplate is invalid.")


else:
    print("The numberplate is invalid.")

