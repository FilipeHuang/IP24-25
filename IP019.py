r1 = float(input())
x1 = float(input())
y1 = float(input())
r2 = float(input())
x2 = float(input())
y2 = float(input())
if (x1-x2)**2+(y1-y2)**2 == (r1+r2)**2 or (x1-x2)**2+(y1-y2)**2 == (r1-r2)**2:
    print("The circles are tangent.")
else:
    print("The circles are not tangent.")