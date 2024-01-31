r = ""
n = int(input("Enter the number to convert: "))
nb  = 2
q = n
res = q % nb
r = str(res) + r
q = q // nb
while q != 0:
    res = q % nb
    r = str(res) + r
    q = q // nb
print(r)