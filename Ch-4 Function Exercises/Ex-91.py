def operator(o : str) -> int:
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "^":
        return 3
    else:
        return -1
    
def main():
    o = input("Enter an operator: ")
    print(f"The precedence of the operator is {operator(o)}")

main()
