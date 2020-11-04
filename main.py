

from colorama import init, Fore, Back, Style
init()
import math


option = int(input())


if option == 1:
    firstTask( a=1, b=1, c=1 )
elif option == 2:
    secondTask( a = 1, b = 1, c = 1 )
elif option == 3:
    thirdTask( a = 1, b = 1, c = 1, d = 1 )
elif option == 4:
    fourthTask( a = 1, b = 1, c = 1, d = 1 )
elif option == 5:
    fivthTask( number = 1 )


def firstTask( a, b, c ):
    a = float(input('Перша сторона: '))
    b = float(input('Друга сторона: '))
    c = float(input('Третя сторона: '))

    if a == b or a == c or a == c:
        print(Style.BRIGHT + Fore.GREEN + 'Трикутник рівнобедрений')
    else:
        print(Fore.RED + 'Some error was occurupted!')


def secondTask( a, b, c ):
    if c**2 == (a**2 + b**2) or a**2 == (c**2 + b**2) or b**2 == (c**2 + a**2):
        print(Fore.GREEN + 'Трикутник прямокутний')
    else:
        print(Fore.RED + 'Помилка...')


def thirdTask( a, b, c, d ):
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))


    if a == b or b == c or c == d or a == d or c == d or b == d:
        print(Fore.GREEN + 'Так, с цих відрізків можливо скласти паралелограм!') 
    else:
        print(Fore.RED + "Неможливо з таких відрізків скласти паралелограм")
    


def fourthTask( width1, height1, width2, height2 ):
    width1 = float(input())
    height1 = float(input())
    width2 = float(input())
    height2 = float(input())

    if width1 > width2 and height1 > height2:
        print(Fore.GREEN + 'Перший прямокутник більший за другий!')
    elif width2 > width1 and height2 > height1 :
        print('Другий прямокутник більший за перший!')
    else:
        print(Fore.RED + 'Some error was occurupted!')


def fivthTask( number ):
    number = int(input())

    if number >= 1 and number <= 2:
        print(Fore.GREEN + 'Winter')
    elif number >= 3 and number <= 5:
        print('Spring')
    elif number >= 6 and number <= 8:
        print('Summer')
    elif number >= 9 and number <= 11:
        print('Autumn')
    elif number == 12:
        print('Winter')
    else:
        print(Fore.RED + 'Some error was occurupted!')


