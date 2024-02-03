m = int(input("Enter the Air Time in minutes: "))
t = int(input("Enter the number of text messages: "))

print("""Base Charge: $15.00
    
        Additional Minutes Charge: $0.25 per minute
        
        Additional Text Messages Charge: $0.15 per text message
        
        911 Fee: $0.44
        
        Sales Tax: 5%""")

c = 0.25*(m-50)
tc = 0.15*(t-50)
if m > 50:
    print("Additional Minutes Charge: $", format(c, '.2f'))

elif t > 50:
    print(f"Additional Text Messages Charge: ${format(tc, '.2f')}")


total = 1.05*(15 + c + tc + 0.44) 
print(f"Total Charge: ${format(total, '.2f')}")

