from itertools import count
from math import factorial

while True:

    def fact():
        for el in count(1):
            yield factorial(el)

    factor = fact()
    chet = 0
    predel = int(input('Введите число, до которого считать факториал: '))

    for fct in factor:
        if chet == predel:
            break
        else:
            chet += 1
            print(f'Факториал числа {chet} равен {fct}')

    again = input('Желаете продолжить (д/н)? ')
    if again == 'н':
        break