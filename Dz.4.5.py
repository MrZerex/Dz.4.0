from functools import reduce

def result(el1, el2):
    return el1 * el2

print(reduce(result, [el for el in range(100, 1001, 2)]))