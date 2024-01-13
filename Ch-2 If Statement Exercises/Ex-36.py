i = input("Enter the letter: ")
if i in "aeiou":
    print("The letter is vowel.")
elif i == 'y':
    print("The letter is sometimes vowel, sometimes consonant.")
else:
    print("The letter is consonant.")