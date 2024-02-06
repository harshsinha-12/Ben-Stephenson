def min_max_lst():
    lst : list = []
    while True:
        num : int = int(input("Enter a number (0 to stop): "))
        if num == 0:
            break
        lst.append(num)

    if len(lst) < 4:
        return None

    min_num : int = min(lst)
    max_num : int = max(lst)
    lst.remove(min_num)
    lst.remove(max_num)
    return lst  

def main():
    result = min_max_lst()
    if result is None:
        print("List must have at least 4 elements.")
    else:
        print("List:", result)

main()
