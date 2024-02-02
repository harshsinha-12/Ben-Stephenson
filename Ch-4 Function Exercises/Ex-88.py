def triangle(a : float,b : float,c : float) -> bool:
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False
def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))
    if triangle(a,b,c):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
main()