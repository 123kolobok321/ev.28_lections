# while <expression>:
    # <body>

# i = 0
# while i < 10:
#     i += 1 # i = i + 1
#     print(f'Цикл сработал {i} раз!') -  будет работать пока будет True

# ls = list(range(1, 51))
# print(ls.reverse())
# while ls:
#     print(ls.pop())

# name1 = ''
# name2 = ''
# i = 0
# while name1.lower() != 'john' and name2.lower() != 'raychel':
#     name1 = input('Vvedite imya1:')
#     name2 = input('Vvedite imya2:')
#     print()
#     if i >= 5:
#         print('Цикл остановлен!')
#         break # принудительная остановка
#     i += 1
# else:   # который сработает если в вайл прилетит false

#     print('Ты угодал!!!')

#################################################################

# user = {'username': 'JohnSnow', 'password': 'ilovepython123'}
# i = 3
# password = None
# while password := input(f'{user["username"]} vvedite parol\':') != user['password']:
    
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany!!!')
#         break
#     # i -= 1
# else:
#     print(f'{["username"]} vy uspeshno zashli v sistemu!!')


#################################################### for

#for <variable> in <iterable object>:
    #<body>

# list_ = [0,1,2,3,4,5,6,7,8,9]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# a,b,c = 1,2,3
# print(a,b,c)


# import random
# ls = []
# for x in range(1, 101):
#     ls.append(random.randint(1, 50))

# print(len(ls))
# ls = set(ls)
# ls = list(ls)
# print(ls)
# print(len(ls))

# ls = ['Tirion', 'Bilal', 'Sansa', 'Jamie', 'Eddart']
# for x in ls:
#     if x == 'Bilal':
#         continue
#     print(f'Hello MR/Mrs {x}!')


# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
    


# число 100
# 1,2,4,5,10
# 20,25,50,100
# 100,50,25,20,10

# num = 888_999_000_000_000
# res = []

# for x in range(1, int(num ** 0.5) + 1):
#     if num% x == 0:
#         res.extend({x, num // x})
# res.sort()
# print(res)







# klub = {'Мурату': 24, 'Эржану': 21, 'Карине': 24, 'Алтынай': 17, 'Айбеку': 16}
# for x in klub:
#   if x == 17:
#     print('Вам нельзя в клуб!!')
  



# x = int(input()) 
# y = int(input()) 
# if x%y == 0: 
#     print("%d делится на %d" % (x,y)) 
#     print("Частное: %d" % (x//y)) 
# else: print("%d не делится на %d" % (x,y)) 
# print("Частное: %d" % (x//y)) 
# print("Остаток: %d" % (x%y))


# x = int(input()) 
# y = int(input()) 
# if x % y == 0: 
#     print('x делится на y') 
#     d = x//y 
#     print(f'Частное: {d}') 
# else: 
#     print('x не делится на y') 
#     a = x // y 
#     print(f'Частное: {a}') 
#     b = x % y 
#     print(f'Остаток: {b}')






# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')



# year = int(input('vvedite god:')) 
# if year%4 == 0 and year%100 != 0 : 
#     print('YES') 
# elif year%400 == 0: 
#     print('YES') 
# else: 
#     print('NO')


# nums = [1, 15, 36, 88]
# target = 15
# if target in nums:
#     print('Да')
# else:
#     print('Нет') # 65 90 # 97 122

# print(ord('z')) 

# num = int(input())
# if (num >= 65 and num <= 90) or (num >= 97 and num <= 122):
#     print(f'Это буква "{chr(num)}"')
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')


# greeting = input()
# if greeting == ('Hi'):
#     print('Привет!')
# else:
#     print('NO')




# count = 0
# number = input()
# if number.isdigit():
#     print(number)
# else:
#     print(count)



















