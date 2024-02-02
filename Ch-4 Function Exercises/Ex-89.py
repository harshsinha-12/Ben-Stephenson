# Write a function that accepts a string and returns a string with the first letter of each word capitalized.
def capitalize(string: str) -> str: 
    for ch in range(1, len(string) - 1): 
        if string[ch-1] == " " and string[ch+1] == " " and string[ch] == "i":
            string = string[:ch] + string[ch].capitalize() + string[ch+1:]
    string = string[0].capitalize() + string[1:]
    return string

def main():
    string = input("Enter a string: ")
    print(capitalize(string))

main()