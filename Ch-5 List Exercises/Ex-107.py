def duplicates(lst : list)-> list:
    lst = []
    while True:
        a : str = input("Enter the elements, enter enter to end input: ")
        if a == '':
            break
        lst.append(a)
    return list(set(lst))

def main():
    print("List:", duplicates([]))

main()