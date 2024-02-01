def number(a):
    while a > 0 and a < 13:
        if a == 1:
            return "First"
        elif a == 2:
            return "Second"
        elif a == 3:
            return "Third"
        elif a == 4:
            return "Fourth"
        elif a == 5:
            return "Fifth"
        elif a == 6:
            return "Sixth"
        elif a == 7:
            return "Seventh"
        elif a == 8:
            return "Eighth"
        elif a == 9:
            return "Ninth"
        elif a == 10:
            return "Tenth"
        elif a == 11:
            return "Eleventh"
        elif a == 12:
            return "Twelfth"
        else:
            return ""


def main():
    a = int(input("Enter the number to convert: "))
    print(number(a))

main()