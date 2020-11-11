
print('Task #177')

number = int(input())

splittednumber = list(str(number))

if splittednumber[0] == splittednumber[1]:
    print('Первые два цифры равные!')
else:
    print('Первые два числа не равные!')
if splittednumber[1] == splittednumber[2]:
    print('Вторая и третья цифры равные!')
else:
    print('Вторая и третья цифры не равные!')
if splittednumber[2] == splittednumber[3]:
    print('Все цифры чотирёхцифрового числа однаковые!')
if splittednumber[0] == splittednumber[3]:
    print('Первая и последняя цифры одинаковы!')
if splittednumber[1] == splittednumber[3]:
    print('Второе и чётвёртое число одинаковы!')
else:
    print('Цифры в этом числе не одинаковые!')

