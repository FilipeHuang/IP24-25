h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
s = (s1 + s2)%60
m = ((s1 + s2)//60 + m1 + m2)%60
h = (((s1 + s2)//60 + m1 + m2)//60 + h1 + h2)%24
print(f"Take the cake out at {h:02}:{m:02}:{s:02}.")