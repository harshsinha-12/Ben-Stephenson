def fare(d_m):
    return 4 + (d_m // 140) * 0.25 

d = float(input("Enter the distance travelled in km: "))
d_m = d * 1000
print(f"The fare is ${fare(d_m):.2f}")