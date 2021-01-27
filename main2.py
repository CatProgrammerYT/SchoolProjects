ukrlists = ['синій', 'червоний', 'помаранчевий',
            'фіолетовий', 'зелений', 'чорний', 'сірий']
englists = ['blue', 'red', 'orange', 'purple',
            'green', 'black', 'gray']
ukrcolorsInput = input('Колір: ').split()

for ukrcolorsInput in ukrlists:
    for i in ukrlists:
        k = ukrlists.index(ukrcolorsInput)
        englists.pop(k)
print(englists)
