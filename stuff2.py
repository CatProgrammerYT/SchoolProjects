
import random
import math

xa = random.randint(0, 5)
ya = random.randint(0, 5)
xb = random.randint(0, 5)
yb = random.randint(0, 5)
xc = random.randint(0, 5)
yc = random.randint(0, 5)

xa2 = random.randint(0, 5)
ya2 = random.randint(0, 5)
xb2 = random.randint(0, 5)
yb2 = random.randint(0, 5)
xc2 = random.randint(0, 5)
yc2 = random.randint(0, 5)


print((xa, ya), (xb, yb), (xc, yc))
print((xa2, ya2), (xb2, yb2), (xc2, yc2))

def dl(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

AB = dl(xa, ya, xb, yb)
BC = dl(xb, yb, xc, yc)
CA = dl(xc, yc, xa, ya)
BA = dl(xa2, ya2, xb2, yb2)
CB = dl(xb2, yb2, xc2, yc2)
AC = dl(xc2, yc2, xa2, ya2)
p = AB + BC + CA
p2 = BA + CB + AC

if p > p2:
     print('Перший більше!')
elif p2 > p:
     print('Другий більше!')
else:
    print('Вони рівні!')


