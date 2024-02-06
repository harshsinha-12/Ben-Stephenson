def only_words(lst : list)-> list:
    words = []  
    while True:
        a : str = input("Enter the elements, enter enter to end input: ")
        if a == '':
            break
        lst.append(a)
    for i in lst:
        if i.isalpha():
            words.append(i)  
    return words  

def main():
    print("List:", only_words([]))

main()