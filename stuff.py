
import random
import math

xa = float(input('xa = '))
ya = float(input('ya = '))
xb = float(input('xb = '))
yb = float(input('yb = '))
xc = float(input('xc = '))
yc = float(input('yc = '))

print((xa, ya), (xb, yb), (xc, yc))

def dl(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

AB = dl(xa, ya, xb, yb)
BC = dl(xb, yb, xc, yc)
CA = dl(xc, yc, xa, ya)
p = AB + BC + CA
print('P = ', p)
p2 = p/2
print('S = ', math.ceil(p2))
