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
    for i in lst:
        if i < avg:
            below_avg.append(i)
        else:
            above_avg.append(i)
    return [below_avg, above_avg]

def main():
    print("List:", below_above_avg([], [], []))

main()