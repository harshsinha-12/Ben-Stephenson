t = 0
c = 0

g = input("Enter Letter Grade: ")

while g != '0':
    grade = 0
    if g == "A+":
        grade = 4.00
    elif g == "A":
        grade = 4.00
    elif g == "A-":
        grade = 3.70
    elif g == "B+":
        grade = 3.30
    elif g == "B":
        grade = 3.00
    elif g == "B-":
        grade = 2.70
    elif g == "C+":
        grade = 2.30
    elif g == "C":
        grade = 2.00
    elif g == "C-":
        grade = 1.70
    elif g == "D+":
        grade = 1.30
    elif g == "D":
        grade = 1.00
    elif g == "F":  
        grade = 0.00

    t = t + grade
    c = c + 1
    g = input("Enter Letter Grade: ")

print(f"Your GPA is {t/c}.")