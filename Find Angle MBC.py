import math
x=float(input())
y=float(input())
z=math.sqrt((x*x)+(y*y))
q=round(math.degrees(math.asin(x/z)))
print ("%d°" %q)