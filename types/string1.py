# 'String - Строки'
# "Hello world"

#  Hello World
# My name is John Snow


#Строки - набор последовательных символов которые мы используем для хранения и представления текстовой информации

# индексация в строке 
# name = 'John'
#         # J = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name)
# print(name[1])
# str1 =  'kani'
# print(str1[-1], str1[0])



# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# str1 = 'birthday'
# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# # Срезы по индексам
# # [start: end: <step>]
# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])



# text = 'Hello World! My name is John! I\'m King of North'
# print(text[:13])
# print(text[:])
# print(text[::2]) 
# print(text[::-1]

# конкатенация строк(соединение)
# a = 'Hello'
# b = 'world'
# c = ' '
# print(a + c + b)

# экранирование - способ записи символов в строку, которые не возможно ввести с клавиатуры
#-> перенос строки
# \n - перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция
# \f - перевод страницы
# \r - возврат указателя
# print('\vHello \tworld!\nMy name is John Snow')


# Форматирование строк
#1. с помощью %
#2. с использованием .format()
#3. Инерполяция строк (преобразование, f-stroki)


# % 
# name = input('Vvedite imya: ')
# last_name = input('Vvedite Last_name: ')
# # print('Добро пожаловать к нам' +  ' ' + name + ' ' + last_name + '!')
# print('Hello mr/mrs %s %s!' %(name, last_name))

# # .format
# name = input('Vvedite imya: ')
# last_name = input('Vvedite Last_name: ')
# print('Приветствуем Вас, {} {}, в нашем клубе!,' .format(name, last_name))

# f-stroki
# a = input('Enter mr/mrs:')
# name = input('Vvedite imya: ')
# last_name = input('Vvedite Last_name: ')
# print(f'Hello {a} {name} {last_name}! Welcome to the parthy!')


# text = 'Запомни Питтер,  ТТ ттттттс большой силой приходит и большая ответственность.'
# reversed_text = text[::-1]
# print(reversed_text)
# i = 0
# count_t = 0
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == 'т' or symbol == 'Т':
#         count_t += 1
#     # print(symbol )
#     i +=1 # инкремент i = i + 1 
# print(f'В тексте "т" встретилась {count_t} раз!')
# #print(len(reversed_text))
# #while 


# string = 'Hello'
# print(string[-1] + string[1:-1] + string[0])




# string = "          Как прекрасен этот мир!   "
# print(" " + string.strip(), len(string.strip())) 


# string = " Как прекрасен этот мир! " 
# res = string.strip() 
# print(f'{res}\n{len(res)}')


# def printThese(a,b,c):
#    print(a, "is stored in a")
#    print(b, "is stored in b")
#    print(c, "is stored in c")
# printThese(1,2,3)



# a = [1,2,3]
# b = [*a,4,5,6]
# print(b)





# n = int(input()) 
# if n >= 11 and n <= 14: 
#     print(f'На лугу пасется {n} коров') 
# else: temp = n % 10 
# if temp == 0 or (temp >= 5 and temp <= 9): 
#     print(f'На лугу пасется {n} коров') 
# if temp == 1: 
#     print(f'На лугу пасется {n} корова') 
# if temp >=2 and temp <=4: 
#     print(f'На лугу пасется {n} коровы')









# Cow

# n = int(input()) 
# if n in range(11, 15): 
#     print(f'На лугу пасется {n} коров') 
# else:
#     temp = n % 10
#     if temp in list(range(5, 10)) + [0]: 
#         print(f'На лугу пасется {n} коров') 
#     if temp == 1: 
#         print(f'На лугу пасется {n} корова') 
#     if temp in range(2, 5): 
#         print(f'На лугу пасется {n} коровы')



# list_ = ['hello', 'World'] 
# new_list = [list_[1],list_[0]] 
# print(new_list)


# my_str = "У меня есть кот и кошка"
# # в цикле передаем список (заменяемое, подставляемое) в метод replace
# for x, y in ("кот", "кошка"), ("кошка", "собака"):
#     my_str = my_str.replace(x, y)
# print(my_str) # Выведет "У меня есть собака и собака"
















