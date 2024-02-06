def sorted_list(numbers : list[int])-> list:
    numbers = []
    while True:
        num : int = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        numbers.append(num)
    return sorted(numbers)

def main():
    print("List:", sorted_list([]))

main()



