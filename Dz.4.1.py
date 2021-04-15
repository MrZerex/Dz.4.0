from sys import argv

#Решение при вводе параметров во время выполнения скрипта
#def zarplata():
#    while True:
#        try:
#            chas = int(input('Введите выработку в часах: '))
#            stav = int(input('Введите ставку в час: '))
#            prem = int(input('Введите размер премии: '))
#            break
#        except ValueError:
#            print('Введите целое значение!')
#            continue
#    return print(f'Заработная плата сотрудника равна: {(chas * stav) + prem}')

#Решение при запуске скрипта с параметрами
name, chas, stav, prem = argv
print(f'Скрипт {name} - Заработная плата сотрудника равна: {(int(chas) * int(stav)) + int(prem)}')





