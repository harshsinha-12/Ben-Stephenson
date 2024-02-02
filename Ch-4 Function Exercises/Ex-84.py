def median(a : float,b : float,c : float) -> float:
    lst = [a,b,c]
    lst.sort()
    return lst[1]

def main(): 
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    print(f"The median is {median(a,b,c)}")

main()