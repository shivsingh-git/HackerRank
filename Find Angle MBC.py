import math
x=float(input())
y=float(input())
z=math.sqrt((x*x)+(y*y))                    #calculating sqrt(x^2+y^2)
q=round(math.degrees(math.asin(x/z)))       #required angle is sine_inverse(x/z)-by geometry
print ("%d°" %q)                            #printing the angle with the degree sign
