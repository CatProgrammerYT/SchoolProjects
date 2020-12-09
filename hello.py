S = float(input('S = ')) # 1
p = float(input('p = ')) # 1
n = int(input('n = ')) # 1
s = S # 2
m = S # 4
q = 0
L = float(input('L = ')) # 5
S1 = int(input('S1 = ')) # 4
for i in range(0, n):
    while True:
        i += 1
        S = S + S/100*p
        s = s + S
        if p > L: # 5
            print('На ' + str(i) + ' день, дистанция будет увеличиватся на L, относительно предыдущего дня.  ') # 4
        if S >= S1: # 4
            break
q = S - m # 4
print('Через ' + str(round(i)) + " дней(-я) спортсмен преодолеет расстояние " + str(round(S)) + " км. ")
print('Суммарное расстояние за ' + str(i) + ' дней будет ' + str(round(s)))
print('Через ' + str(x) + ' дней спортсмен преодолеет расстояние в ' + str(round(S1)) + ' км')
print('На ' + str(round(n)) + " день тренировки спортсмен преодолеет расстояние в " + str(round(S)) + " км и это будет больше на " + str(round(q)) + " км чем в начале " + str(round(m)) + ". ")
