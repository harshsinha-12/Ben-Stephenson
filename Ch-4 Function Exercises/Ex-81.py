def hypotenuse(a : float, b : float) -> float:
    return (a**2 + b**2)**0.5

def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    print(f"The length of the hypotenuse is {hypotenuse(a, b)}")

main()