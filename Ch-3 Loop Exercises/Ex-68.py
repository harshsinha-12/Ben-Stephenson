i = input("Enter 8 bits: ")
while i != "":
    if i.count("1") + i.count("0") != 8:
        print("Invalid input.")
    else:
        if i.count("1") % 2 == 0:
            print("Parity bit should be 0.")
        else:
            print("Parity bit should be 1.")
    i = input("Enter 8 bits: ")