from random import randrange

def licence():
    return chr(randrange(65, 91))

def main():
    n = randrange(1000, 10000)
    a = 3
    k = randrange(1,3)
    nl = randrange(100, 1000)
    print("Your licence plate is:")
    for i in range(a):
        print(licence(), end="")
    print("-", end="")
    if k == 1:
        print(n, end=" ")
    else:
        print(nl, end=" ")

main()