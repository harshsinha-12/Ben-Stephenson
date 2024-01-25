print("Original Price\tDiscount Amount \tDiscounted Price")
for i in range(4, 29, 5):
    print(f"{format(i+0.95, '.2f')} \t\t {format(i*0.6, '.2f')} \t\t\t {format(i*0.4, '.2f')}")