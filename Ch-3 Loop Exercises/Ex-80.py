from random import randint

count = 0
outcomes = []
while True:
    a = randint(0,1)
    if a == 0:
        outcome = "Heads"
    else:
        outcome = "Tails"
    outcomes.append(outcome)
    print(outcome)

    if len(outcomes) >= 3:
        if outcomes[-1] == outcomes[-2] == outcomes[-3]:
            break
    count += 1
print(f"It took {count} flips to get 3 consecutive {outcome}'s.")


