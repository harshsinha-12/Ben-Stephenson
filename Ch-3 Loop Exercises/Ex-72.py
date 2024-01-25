a = input("Enter the word: ")
r = ""

for i in range(-1, -len(a)-1, -1):
    r = r + a[i]

if a == r:
    print(f"'{a}' is a palindrome.")
else:
    print(f"'{a}' is not a palindrome.")

