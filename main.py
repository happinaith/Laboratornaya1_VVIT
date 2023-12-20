import math
a = int(input())
b = int(input())
c = int(input())

discr = b**2 - 4*a*c

if discr < 0:
    print("Корней нет")
elif discr == 0:
    print(int(-b/2*a))
else:
    x1 = (-b+math.sqrt(discr))/2*a
    x2 = (-b-math.sqrt(discr))/2*a
    print(int(x1), int(x2))
