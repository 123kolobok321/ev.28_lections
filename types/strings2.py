# str
# ''
# 'Hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# # print(a != b)
# print('abc' == 'abc')
# print(a > b)
# print(a < b)
# print('a') # 97 -> 1100001
# print('h' > 'c')

# print('hello' > 'harry') #True
# print('abc' > 'abc') # False
# len() - возвращает количество символов в строке
# a = 'hello'
# b = 'john snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# >, <, ==, !=, >=, <=

# Методы строк
#replace(old, new, [count]) - меняет в строке символы old на new, если вы укажите count,
# то заменит count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f' result after replace: {result}')

# str1 = 'Hello world! My name is John Snow!'
# res = str1.replace('John Snow', 'Tirion Lanister')
# print(res)

# strip() - Уберает пробельные символы в начале и в конце строки
# rstrip, lstrip 
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))

# print(dir(str))


# isdigit-         проверяет
# isnumetric -   состоит ли наша строка
# isdecimal -    полностью из чисел

# num = input('Vvedite chislo:')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo:')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vveli ne chisla')

# text = '\u0031'
# print(text)
# print(text.isnumeric())
# print(text.isdigit())
# print(text.isdecimal())


#isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского 
# алфавита и киррилицы
# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_2'
# print(str2.isalnum())

# isalpha() -> состоит ли наша строка полностью из символов алфавита

# text = 'Hello world'
# res = text.replace(' ', '')
# print(res)
# print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Mi. My Name'
# print(str1.islower())# false
# print(str1.istitle())
# str2 = 'KOLOBOK'
# print(str2.isupper())




# index(value, [start], [end]) - выводит индекс значения value, которое мы передаем, 
# в нашей строке.

# text = 'Hello john snow'
# print(text.index('john'))

# text = 'Hello world! My name is John Snow!'# o
# res = text.index('o') 
# print(res)# 4
# res = text.index('o', res + 1)
# print(res)#7
# res = text.index('o', res + 1)
# print(res)#25
# res = text.index('o', res + 1)
# print(res)#31

# count(value, [start]) -  считает количество вхождений value в нашу строку

# text = 'hello o o o hello'
# print(text.count('o')) 
# print(text.count('hello'))
# print(text.count('hffhfg'))

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части строк сохраняются в типе list

# text = 'Let me speak by my heart in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# print(len(res))
# a = '#hello#hello#hello#hello'
# res = a[1:].split('#')
# print(res)

# 'connector'.join(list) -> соендиняет по connector строки которые находились в list


# text = 'Let me speak by my heart in English! Cause my name is John Snow!'
# res = text.split(' ')
# print(res)
# str1 = ' '.join(res)
# print(str1)

# find(value, [start], [end]) - делает тоже самое что и index, но если не нашёл то вернётся -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('kolo'), type(text.find('kolo')))
# print('John Snow')

# swapcase() - переводит все символы в противоположный регистр
# upper() - переводит все в верхний регистр
# lower()- переводит все в нижний регистр

# text = 'Hello WorLD, JOHN snow'
# print(f'Original:{text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())


# capitalize() - переводит самый первый символ в верхний регистр
# litle() - переводит первые символы всех слов в верхний регистр

      #john.capitalize() -> John

# name = input('Vvedite imya:').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'john edart snow'
# print(fio.title())

#print(dir(str))- показывает какие есть команды и методы и функции












