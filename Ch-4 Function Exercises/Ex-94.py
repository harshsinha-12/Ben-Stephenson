from random import randrange

def password():
    return chr(randrange(33, 127))


def main():
    s = 7
    l = 10

    r = randrange(s, l + 1)
    print("Your password is:")
    for i in range(r):
        print(password(), end="")
    print()

main()