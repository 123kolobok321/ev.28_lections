# find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# rfind(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
# index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
# rindex(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
# replace(шаблон, замена) - Замена шаблона
# split(символ) - Разбиение строки по разделителю
# upper() - Преобразование строки к верхнему регистру
# lower() - Преобразование строки к нижнему регистру 
# swapcase() - Переводит символы нижнего регистра в верхний, а верхнего – в нижний
# startswith(str) - Начинается ли строка с шаблона str
# title() - Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
# capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
# endswith(str) - Заканчивается ли строка S шаблоном str
# isdigit() - Состоит ли строка из цифр
# isalpha() - Состоит ли строка из букв
# isalnum() - Состоит ли строка из цифр или букв
# islower() - Состоит ли строка из символов в нижнем регистре
# isupper() - Состоит ли строка из символов в верхнем регистре
# isspace() - Состоит ли строка из неотображаемых символов (пробелов, табуляции)
# istitle() - Начинаются ли слова в строке с заглавной буквы

# stroka = 'Makers Bootcamp'
# print(stroka.find('Bootcamp'))

# stroka = 'Makers Bootcamp'
# print(stroka.rfind('oot'))

# stroka = 'Makers Bootcamp'
# print(stroka.index('oot'))

# stroka = 'Makers Bootcamp'
# print(stroka.rindex('oot'))

# stroka = 'Makers Bootcamp'
# res = stroka.replace('Makers Bootcamp', 'Makakers Bezshtans')
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.split(' ')
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.lower()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.swapcase()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.startswith('Bootcamp')
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.title()
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.capitalize()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.endswith('Makers')
# print(res)

# stroka = '43842780374'
# res = stroka.isdigit()
# print(res)

# stroka = 'MakersBootcampOnlyOneInTheWorld'
# res = stroka.isalpha()
# print(res)

# stroka = 'Makers2Bootcamp3Only4One5In6The7World'
# res = stroka.isalnum()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# res1 = res.islower()
# print(res1)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# res1 = res.isupper()
# print(res1)

# stroka = '              ' # пробелы и табуляция
# res = stroka.isspace()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.istitle()
# print(res)

