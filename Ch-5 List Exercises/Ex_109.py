def proper_divisors(n: int)-> list:
    lst : list= []
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
    return lst

def main():
    n = int(input("Enter a number: "))
    print("Proper divisors:", proper_divisors(n))

main()