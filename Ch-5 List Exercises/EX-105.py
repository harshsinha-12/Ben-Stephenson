def reverse(lst : list)-> list:
    lst = []
    while True:
        num : int = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        lst.append(num)
    return lst[::-1]

def main():
    print("List:", reverse([]))

main()