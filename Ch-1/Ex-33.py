day_old = int(input("Enter the number of day old breads: "))
regular_price = 3.49
discount = 0.6  
discount_price = regular_price * discount
print(f"The regular price is ${format(regular_price, '.2f')}.")
print(f"The discount price is ${format(discount_price, '.2f')}.")
total_price = day_old * discount_price
print(f"The total price is ${format(total_price, '.2f')}.")