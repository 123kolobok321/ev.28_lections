# Set() - Множества
# Это изменяемый неуплрядочный, итерируемый неиндексируемый тип данных

#  множества хранят в себе Только не изменяемые типы данных

# a = 'ggffhdj'
# print(hash(a))

# a = ['ddd']
# print(hash(a))

# 1 -> set()

# a = set([1,2,3,4])
# print(a)

# a = set({1:2, 3:4})
# print(a)

# 2 -> {}
# se2 = {1, 2, 4}
# print(se2)

# set1 = {1, 2, 2, 2, 3}
# print(set1)

# set1 = {0,}
# print(set1)

# set1 = {1, 0, True, False}
# print(set1)

# a = 0
# print(bool(a))

# методы SET

# add -> для добавления

# set1 = {1, 2, 3}
# # set1.add(4)
# # print(set1)
# # set1.add((1, 2, 3, 4, 5))
# # print(set1)

# # update /  он может добавлять но не повторяя имеющиеся добавляет все итерируемые

# set1.update({3 : '1', 4:'5'}) 
# print(set1)
# set1.update('string', {1,2,3,4,5,6,7})
# print(set1)

# set1.update([1,2,3,45,6])
# print(set1)

# Удоление в set
# clear - оно очещает все множества
# remove(element) - удоляет элемент если его нет выдает ошибку
# discard(element) - если элемента нету ничего не происходит
# pop() - удоляет из set(FIFO) first in first out


# set1 = {1,2,3,4,5}
# set1.remove(2)
# print(set1)
# # set1.clear()
# print(set1)
# # set1.discard(5)
# print(set1)
# print(set1.pop())
# print(set1)
# set1 = {1,2,3,4,5}
# set1.update('lol')
# print(set1.pop())
# print(set1)
# difference - выводит отличие
# set1 = {1,2,3,4}
# set2 = {2,3,5,7}
# # print(set1.difference(set2))
# # print(set1 - set2)
# # print(set2.difference(set1))
# # a = set1.symmetric_difference(set2)
# # print(set1.symmetric_difference(set2))
# # print(set1^set2)

# print(set1.symmetric_difference_update(set2))


# print(set1.intersection(set2))
# print(set1&set2)

# print(set1.union(set2))
# print(set1 | set2)

# set1 = {1,2,3,4}
# set2 = {2,3,5,7}
# print(set1.difference(set2))


# a = [1,2,3,4]
# b = [2,3,5,7]

# set1 = set(a)
# set2 = set(b)
# print(set1.difference(set2))


#_________________________________________________________

                                   ### Задачки ###

# set1 = set(['White', 'Black', 'Red'])
# set2 = set(['Red', 'Green'])
# print(set1^set2)


# num = list(input())
# print(len(num) == len(set(num)))

# tuple - неизменяймый, индексируемый, итерируемый, упорядоченый тип данных
# index(element) - возвращает индекс этого элемента в кортеж 
# литералы ()
# a = (True, 'a', 1, 1, 1, 4)
# # print(a, type(a))
# b = tuple()
# print(a.index(1))
# # count(element) - возвращает число вхождений этого элемента в кортеж
# print(a.count(1)) 


####################################################

# tuple = (1,2,3,4,5,6,7,8)
# target = 5
# index of target
# tuple.index(target)
#




























































































































































