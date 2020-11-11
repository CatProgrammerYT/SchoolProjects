
print('Task #159')
number = int(input())

splittednumber = list(str(number))

#print(splittednumber)

if splittednumber[0] > splittednumber[1]:
    print('1')
elif splittednumber[1] > splittednumber[0]:
    print('2')
else:
    print('They are equal!')
