from random import randint, randrange

num_items = 100

max_value = randrange(1, num_items + 1)
print(max_value)

num_updates = 0

for i in range(1, num_items):
    current = randint(1, num_items)

    if current > max_value:
        print(f"New maximum found: {current}")
        max_value = current
        num_updates += 1
    else:
        print(f"Maximum found: {max_value}")
    
print(f"Maximum value found: {max_value}")
print(f"Maximum updated {num_updates} times")
