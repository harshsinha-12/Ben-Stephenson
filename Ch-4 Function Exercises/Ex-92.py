def prime():
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

def main():
    global n
    n = int(input("Enter a number: "))
    prime()

main()