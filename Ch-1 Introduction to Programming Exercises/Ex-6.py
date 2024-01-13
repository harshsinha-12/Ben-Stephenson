f = float(input("Enter the meal amount:"))
sgst = f * 0.025
cgst = f * 0.025
tax = sgst + cgst
tip = f * 0.18
gt = f + tax + tip
print(f"The tax is {format(tax, '.2f')} and the tip is {format(tip, '.2f')} and the grand total for bill is {format(gt, '.2f')}.")