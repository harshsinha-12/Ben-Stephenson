def prime(n: int) -> bool:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False  # Not a prime number
        return True  # Is a prime number
    return False  # Numbers less than 2 are not prime

def next_prime(a: int) -> int:
    while True:
        a += 1
        if prime(a):
            return a

def main():
    try:
        a = int(input("Enter a number to find the next prime: "))
        print(f"The next prime number is {next_prime(a)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
