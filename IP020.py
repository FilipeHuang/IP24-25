import math
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if d == 0:
    r = -b/(2*a)
    print(f"R = {round(r,2)}")
elif d > 0:
    r1 = (-b+math.sqrt(d))/(2*a)
    r2 = (-b-math.sqrt(d))/(2*a)
    print(f"R1 = {round(r1,2)}\nR2 = {round(r2,2)}")
else:
    r1 = -b/(2*a)
    r2 = -b/(2*a)
    print(f"R1 = {round(r1,2)} + {round(math.sqrt(-d)/(2*a),2)}i\nR2 = {round(r2,2)} - {round(math.sqrt(-d)/(2*a),2)}i")