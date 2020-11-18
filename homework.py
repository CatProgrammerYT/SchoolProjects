S = float(input("S = "))
P = float(input("P = "))
N = float(input("N = "))
year = 0

while True:
    S = S * P
    year += 1
    print(S, year)
    if S >= N: break
