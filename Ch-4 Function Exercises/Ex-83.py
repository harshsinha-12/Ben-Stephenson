def shipping_cost(n):
    return 10.95 + (2.95 * (n - 1))

def main():
    n = int(input("Enter the number of items: "))
    print(f"The shipping cost is ${shipping_cost(n):.2f}")