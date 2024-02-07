def lottery():
    from random import randint
    return [randint(1, 49) for _ in range(6)]

print(lottery())