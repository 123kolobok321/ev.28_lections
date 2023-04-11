#Типы данных числа -> int, float

# = -> оператор присваения
# variable (переменная)
# num = 5 
# print(num)# 5
# num = 79 #переопределение
# print(num) # 79


#abc -> нижний регистр
# ABC -> верхний регистр

# # pep8
# tomorrow_day = '10.03.2023' # Snake case
# tomorrowDay = '10.03.2023' # Camel case

# num1 = 5 
# num2 = 15
# result = num1 + num2
# print('Summa', result)

# - 
# num1 = input('Enter the num1:')
# num2 = input('Enter the num2:')
# num1 int(num1)
# num2 int(num2)
# print(num2, '-', num1, '=', num2  - num1)

# *
# num1 = int(input('Enter the num1:'))
# num2 = int(input('Enter the num2:'))
# print(num1, '*', num2, '=', num1 * num2)


# / and //and %
# / - обычное деление
# // - деление без остатка 
# % - модульное деление (получение остатка от деления)

# num1 = 7
# num2 = 3
# print('/', num1 / num2)
# print('//', num1 // num2)
# print('%', num % num2)


# ** -> возведение в степень
# print(5 ** 2)
# print(16 ** 55)


# print(9 ** 0.5) #квадратный корень 

# pow -> возведение в степень
# pow (num1, num2 <mod>)
# num1 = 5
# num2 = 10
# print(num1 ** num2)
# print(pow(5 ,10, 65))
# print(5 ** 10 % 65)

# a = 5
# b = 2
# res = pow (a, b, 12)
# print(res)

# round() - округления числа с плавующей точкой

# a = 5.728232

# print(round(a, 2))

# abs() - абсолютное значение числа -> abs(-5) -> 5

# a = abs(-16)
# b = abs(15)
# print(a, b)

# divmod(a, b) - она выводит два числа, первое число это результат целочисленого деления (//) a на b, а второе это модульное деление (%)


# res = divmod(5, 2)
# print(res)
# print((5 // 2, 5 % 2))


# import math 
# a = 5
# print(round(math.sqrt(a), 2))

# print(9 ** 0.5)



# множественное присваение
# оператор присвоения(=)
# a = 5
# b = 15
# print('a:', a, 'b:', b) 

# a = 5 
# b = 15
# c = None

# c = a
# a = b
# b = c 

# a, b = b, a 


# num1, num2, num3 = input('Num1:'), input('Num2:'), input('Num3:')
# print(num1)
# print(num2)
# print(num3) 
# from math import pi
# r = int(input('Vvedite radius:'))
# res_P = 2 * r * pi
# res_S = pi * r ** 2
# print('S okruzhnasti:',round(res_S))
# print('P okruzhnasti:', round(res_P))

# from random import randint

# # print(randint(1, 10))


# name = input('Vvedite svoe imya:')
# last_name = input('Vvedite svoyu familiyu:')
# num = randint(1_000_000, 9_999_999)
# print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)

# from random import randint

# num = randint(1, 10)
# print(num) 
# i = 0 
# while i < 3:
#     guess = int(input('Ugodai chislo:'))
#     if guess == num:
#         print('Yuo win')
#         break
    
#     #i = i + 1
#     i += 1 # increment


# task 16
# num = 4
# p = (num + num) * 2
# s = num ** 2
# print(p, s)



# task 17
# length = 4
# heigth = 8
# p = (length + heigth) * 2
# s = length * heigth
# print(p, s)

# length = 12 
# height = 9 
# per = (length+height)*2 
# s = length * height 
# print(per,s)

# task 18
# pi = 3.14
# radius = 6
# p1 = 2 * pi * radius
# p2 = pi * radius ** 2
# print(p1, p2)

# task 19
# num1 = 10
# num2 = 10
# pop = pow(num1, num2)
# pop2 = pow(num2, num1)
# print(pop, pop2)


# x = int()
# y = int()
# resault = x % y
# print(resault)
# print('Частное:')
# print('Остаток:')
# print('Частное:')










