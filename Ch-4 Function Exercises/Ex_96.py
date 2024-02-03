def goodpassword_generator(p: str) -> bool:
    if len(p) < 8:
        return False
    if not any(i.isdigit() for i in p):
        return False
    if not any(i.isupper() for i in p):
        return False
    if not any(i.islower() for i in p):
        return False
    return True

def main(p : str) -> None:
    p = input("Enter a password: ")
    if goodpassword_generator(p):
        print("Valid password")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main("p")