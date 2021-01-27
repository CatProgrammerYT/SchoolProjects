listMemes = ['morshu', 'globglobgab',
             'money add then multiply', 'skibidi boom',
             'THICC', 'RTX on']
inputWord = input()

print('Old list: ')
print(listMemes)
print('---------------')

if inputWord in listMemes:
    listMemes.remove(inputWord)
    print(listMemes)
else:
    print('There is not word in list with name ' + inputWord)
