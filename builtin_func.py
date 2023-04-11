## Встроенные функции

## Анонимная функция -lambda(Обычная функция с одной особенностью, у неё нет имени)
## Принимает сколько угодно параметров, но всегда возвращает одно выражение

# def hello():
#     return 'hello'
# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5,5,5))



# x = lambda num1, num2, degree=None: (num1 * num2) ** degree if degree else num1 * num2
# print(x(2, 2, 3))
# print(x(5, 5))


# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))

# list_ = ['hello', 'bil', 'john','daniel', 'vlad']
# a = sorted(list_, key=len, reverse=True)
# print(a)

# dict_ = {'john': 500, 'triton': 160_000, 'tom': 150, 'sanchar': 20, 'ayana': 100_000}
# new_dict = dict(sorted(dict_.items(), key=lambda x: x[1], reverse=True))
# print(new_dict)

# print(dict_.items())

"""
map(function,iterable) - применяется к каждому элементу внутри iterable функцию, которую мы ей передаем в function
закидывая в результат те данные, которые возвращает функция Врезультате мы получаем mapobject(iterator), в котором
хранятся все наши данные.
"""
# ls = ['one', 'two', 'three', 'four']

# new_list = list(map(lambda x: x.capitalize(), ls))
# print(new_list)

# ls = ['1', '2', '3']
# new_list = list(map(int, ls))
# print(new_list)

# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']
# new_names = list(map(lambda x: f'hello, mr/mrs {x}', names))
# print(new_names)


'''
Функция высшего порядка - функция, которая принимает в качестве аргумента другую функцию
'''
'''
filter(function, iterable) - применяет ко всем элементам iterable функцию, которую мы передали и возвращает 
filterobject(итератор) только с теми элементами, для которых функция вернула True
'''

# ls = ['one', 'lili', 'oleg', 'billi', 'tirion']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)


"""
enumerate(iterable)- пронумеровывает каждый элемент внутри iterable её собственным индексом
"""

# ls = ['str1', 'str2', 'str3']
# new_list = list(enumerate(ls))
# print(new_list)


# zip(iterables) - она соендиняет каждый элемент итерируемых обьектов между собой 
# в тип данных tuple и возвращает итератор

# ls1 = [1,2,3]
# ls2 = [100,200,300]

# res = dict(zip(ls1, ls2)).items()
# print(res)

# ls1 = [1,2,3,4,5]
# ls2 = [100,200,300,400,500,600]
# ls3 = [10,20,30]

# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {'octbr': ['bishkek_octbr', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.0.12'],
#       '1may': ['bishkek_1may', 'Jibek-Jolu 212', 'Goin', 'Ceee', '11.255.0.12'],
#         'svrdl': ['bishkek_svrdl', 'Jibek-Jolu 212', 'Go', 'Cerr', '14.255.0.12']}
# bishkek_date = {}
# for k in data:
#     bishkek_date[k] = dict(zip(d_keys, data[k]))

# print(bishkek_date)

########################################

# all(), any()
# all(Iterable)- Возвращает True , если все элементы итерируемого обьекта истина , иначе False

# ls = [5,6,7]
# print(all(ls)) # -> True

# ip = '10.255.0.155' # True
# ip1 = '10.124.0y.202' # False

# result = all(x.isdigit() for x in ip.split('.'))
# result2 = all(x.isdigit() for x in ip1.split('.'))
# print(result, result2)


# any - Возвращает True, если хотя бы один один элемент истина


# ls = [1,3,[1,2], 0]
# print(any(ls))


# ignore = ['rm-rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite commandu: ')
# if any(x in command for x in ignore):
#     raise Exception('Block you!')
# print('OK!')

########################################
# for x in repeat('str', 15):
#     print(x)
## Генератор рандомных паролей

# from random import choices
# from string import ascii_letters, digits, punctuation
# from itertools import repeat



# symbol = '_()+-@!#%'
# q_pass = int(input('Vvedite kol-vo paroley: '))

# result = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbol, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of password: {len(result)}')

# from statistics import mean
# avg = mean(len(x) for x in result)
# print(f'Avg len of passwords: {avg}')




































