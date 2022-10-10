# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_fail(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    fail = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in fail:
        x.append(' + ')
    fail = list(itertools.chain(*fail))
    fail[-1] = ' = 0'
    return "".join(map(str, fail)).replace(' 1*x',' x')


ratios = get_ratios(k)
fail1 = get_fail(k, ratios)
print(fail1)

with open('new_fail.txt', 'w') as data:
    data.write(fail1)


