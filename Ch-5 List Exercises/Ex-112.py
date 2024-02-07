def below_above_avg(lst : list, below_avg: list, above_avg:list)->list:
    lst = []
    below_avg = []
    above_avg = []
    while True:
        a : str = input("Enter the elements, enter enter to end input: ")
        if a == '':
            break
        lst.append(int(a))
    avg : float = sum(lst) / len(lst)
    print("Average is : ", avg)
    for i in lst:
        if i < avg:
            below_avg.append(i)
        else:
            above_avg.append(i)
    return [lst, below_avg, above_avg]


def main():
    lst, below_avg, above_avg = below_above_avg([], [], [])
    print("List:", lst)
    print("Below Average List:", below_avg)
    print("Above Average List:", above_avg)

main()

