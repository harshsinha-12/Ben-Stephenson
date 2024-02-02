def isInteger(s : str) -> bool:
    s = s.strip()
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

def main():
    s = input("Enter a string: ")
    if isInteger(s):
        print("The string represents an integer.")
    else:
        print("The string does not represent an integer.")

main()