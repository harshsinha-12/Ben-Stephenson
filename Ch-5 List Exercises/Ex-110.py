from Ex_109 import proper_divisors

def perfect_numbers(n: int) -> list:
    lst : list = []
    for i in range(1, n+1):
        if sum(proper_divisors(i)) == i:
            lst.append(i)
            print(i)
    return lst

def main():
    n = int(input("Enter a number: "))
    print("Perfect numbers:", perfect_numbers(n))

main()  