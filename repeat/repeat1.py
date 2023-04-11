# num1 = 1
# while num1 >= 0:
#     num1 = input('Vvedite cheslo:') # int('54') # 54t
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('Встретилось отрицательное число!')







# num1 = 1

# while num1 >= 0:
#     num1 = input('Vvedite chislo: ')
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('Встретилось отрицательное число')


#-----------------------------------

# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))

# ls.sort()
# print(ls, len(ls))
# ls1 = []
# if x not in ls:
#     ls.append(ls1)
# print(ls1,len(ls1))



# from random import randint

# ls = []
# for x in range(0, 100):
#     ls.append(randint(0, 100))

# ls.sort()
# print(ls, len(ls))


# res = []
# for x in ls:
#     if x not in res:
#         res.append(x)

# print(res, len(res))

#-----------------------------------------------
# task 24 chees
# x1 = int(input('Vvedite 1 coordinatu gde stoit ladya:'))
# y1 = int(input('Vvedite 2 coordinatu gde stoit ladya:'))
# ladya = [x1, y1] # 2, 5
# x2 = int(input('Vvedite 1 coordinatu kuda idet ladya:'))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya:'))
# target = [x2, y2] # 4, 6


# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')


# x1 = int(input('Vvedite 1 coordinatu gde stoit ladya:'))
# y1 = int(input('Vvedite 2 coordinatu gde stoit ladya:'))
# ladya = [x1, y1] # 2, 5
# x2 = int(input('Vvedite 1 coordinatu kuda idet ladya:'))
# y2 = int(input('Vvedite 2 coordinatu kuda idet ladya:'))
# target = [x2, y2] # 4, 6


# if x2 - x1 == y2 - y1:
#     print('YES')
# else:
#     print('NO')



# Цикл for
# task 4

# list_ = ['World', 'Hello']
# new_list = []
# for 
# print(list_)
















#-----------------


# import random 
# ls = ['Plov', 'Besh-Barmak','Kuurdak', 'Oromo', 'Lagman']
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0


# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
#     #print(meal)
#     if meal.lower() == 'plov':
#         p += 1
#     elif meal.lower() == 'besh-barmak':
#         b += 1
#     elif meal.lower() == 'kuurdak':
#         k += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     elif meal.lower() == 'lagman':
#         l += 1
# ls.sort()
# print('Результаты голодных игр:')
# print(f'Plov: {p}\nBesh- Barmak: {b}\nKuurdak: {k}\nOromo: {o}\nLagman: {l}')


#----------------------------------==



# https://t.me/c/1708289512/236


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.




# 1) nums = [2, 7,11, 15]
# target = 9
# 0.1 -------------------- 2+7=9
                   # 9-2=7

# 2) nums = [4, 11, 2, 5, 1, 6]
# target = 8
# 2,5 ------------------ 2+6=8
                     #8-4=4
                    #8-11=-3
                     #8-2=6


# nums = [2, 7, 11, 15]
# target = 9

# nums = [4, 11, 2, 5, 1, 6]
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]: # это для второй задачи
#             print(f'Otvet: {i}, {nums.index(num)}')
#             break

    




























































































