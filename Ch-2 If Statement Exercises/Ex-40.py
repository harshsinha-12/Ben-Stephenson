s1 = float(input("Enter the length of the first side of the triangle: "))
s2 = float(input("Enter the length of the second side of the triangle: "))
s3 = float(input("Enter the length of the third side of the triangle: "))
if s1 == s2 == s3:
    print("The triangle is equilateral.")
elif s1 == s2 or s2 == s3 or s3 == s1:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
    