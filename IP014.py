import math
a = input()
r = float(input())
if a == "1":
    print(f"Diameter: {2*r:.2f}")
elif a == "2":
    print(f"Perimeter: {2*r*math.pi:.2f}")
elif a == "3":
    print(f"Area: {r**2*math.pi:.2f}")
else:
    print("Invalid Option.")