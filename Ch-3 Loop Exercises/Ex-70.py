a = input("Enter the text: ")   

for i in range(len(a)):
    if a[i] == " ":
        print(" ", end = "")
    elif ord(a[i]) >= 97 and ord(a[i]) < 120:
        print(chr(ord(a[i]) + 3), end = "")
    elif ord(a[i]) >= 65 and ord(a[i]) < 88:
        print(chr(ord(a[i]) + 3), end = "")
    elif ord(a[i]) == 120:
        print("a", end = "")
    elif ord(a[i]) == 121:
        print("b", end = "")
    elif ord(a[i]) == 122:
        print("c", end = "")
    elif ord(a[i]) == 88:
        print("A", end = "")
    elif ord(a[i]) == 89:
        print("B", end = "")
    elif ord(a[i]) == 90:
        print("C", end = "")
    else:
        print(a[i], end = "")
