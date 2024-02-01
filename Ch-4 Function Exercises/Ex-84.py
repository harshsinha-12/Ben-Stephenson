def median(a,b,c):
    lst = [a,b,c]
    lst.sort()
    return lst[1]

def main(): 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))

    print(f"The median is {median(a,b,c)}")

main()