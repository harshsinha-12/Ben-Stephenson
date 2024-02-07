def is_sorted(lst):
    return lst == sorted(lst)


def main():
    user_list = input("Enter a list of numbers (separated by spaces): ").split()
    user_list = [int(num) for num in user_list]

    if is_sorted(user_list):
        print("The list is sorted.")
    else:
        print("The list is not sorted.")


main()