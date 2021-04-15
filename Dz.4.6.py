from itertools import count, cycle

while True:
    while True:
        print('Генерация целых чисел, начиная с указананного')
        num = int(input('Введите целое число: '))
        chet = 0
        for el in count(num):
            print(el)
            chet += 1
            if chet >= 10:
                break
        break

    while True:
        print('Повторение элементов списка')
        new_list = input('Введите элементы списка через пробел: ').split()
        chet = 0
        for el in cycle(new_list):
            print(el)
            chet += 1
            if chet >= 15:
                break
        break
    again = input('Желаете продолжить? (д/н) ')
    if again == 'н':
        break