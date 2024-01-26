a = input("Enter the word: ")

a = ''.join(c.lower() for c in a if c.isalpha())


r = ""

for i in range(-1, -len(a)-1, -1):
    r = r + a[i]

if a == r:
    print(f"'{a}' is a palindrome.")
else:
    print(f"'{a}' is not a palindrome.")
