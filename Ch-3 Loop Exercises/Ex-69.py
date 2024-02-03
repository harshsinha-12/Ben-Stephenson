pi: float = 3

for i in range(2, 31, 2):
    if i % 4 == 0:
        pi = pi - (4 / (i * (i + 1) * (i + 2)))
        print(pi)
        print()
    else:
        pi = pi + (4 / (i * (i + 1) * (i + 2)))
        print(pi)
        print()

