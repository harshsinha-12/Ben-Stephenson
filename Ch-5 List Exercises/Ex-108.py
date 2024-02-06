def group_sort(lst_neg: list, lst_pov:list, lst_zero:list)-> list:
    lst_neg = []
    lst_pov = []
    lst_zero = []
    while True:
        num : str = input("Enter a number (blank to stop): ")
        if num == '':
            break
        elif int(num) < 0:
            lst_neg.append(num)
        elif int(num) > 0:
            lst_pov.append(num)
        else:
            lst_zero.append(num)

    return lst_neg + lst_zero + lst_pov

def main():
    print("List:", group_sort(lst_neg=[], lst_pov=[], lst_zero=[]))

main()