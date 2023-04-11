# найти квадрат, куб, результат деления на 100
# num1 = 5 
# -> {'num': 5, '2': 25, '3': 125, '100': 0.05}
# num1 =5
# print({'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 / 100})
# num2 = 16
# print({'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 / 100})
# num3 = 28
# print({'num': num3 '2': num3 ** 2, '3': num3 ** 3, '100': num3 / 100})
# num4 = 1154
# print({'num': num4, '2': num4 ** 2, '3': num4 ** 3, '100': num4 / 100})

# num5 = 31
# print({'num': num5, '2': num5 ** 2, '3': num5 ** 3, '100': num5 / 100})

#  DRY - don't repeat yourself

# num1 = 5
# num2 = 16
# num3 = 28
# num4 = 1154
# num5 = 31

# def operations(num):
#     print({'num': num, '2': num ** 2, '3': num ** 3, '100': num / 100})

# operations(num1)
# operations(num2)
# operations(num3)
# operations(num4)
# operations(num5)

###################################

# Функция - это именнованая часть программы, которая содержит в себе определенный набор инструкций, и может вызываться в других частях программы столько раз сколько угодно

# def name_of_func(<a, b> # параметры):
    # <body> #  код, какая  то логика которая будет давать конечный результат
    # <return> # оператор который помогает вернуть результат

# name_of_func(5,6 # аргументы)

# параментры функции - переменные которые будут принимать данные от пользователя, и хранить в себе эти данные

# аргументы функции - данные которые мы передаем в функцию, в моменте вызова

# print(len('str'))

# ls = [1,2,3,4,5]
# str1 = 'Hello world s vami Kani i John Snow!'

# def our_len(obj):
#     i = 0
#     print(obj)
#     for x in obj:
#         i += 1
#     print(f' result: {i}')

# our_len(ls) # [1,2,3,4,5]
# our_len(str1)


# def isEven(obj):
#     # if obj % 2 == 0:
#     #     return True
#     # else:
#     #     return False
    

#     return True if obj % 2 == 0 else False


# result = isEven(6)
# print(result)
# print(isEven(5))


# list_ = list(range(1, 21))
# print(list_)


# list_ = list(range(0, 101, 2))
# print(list_)

# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# c = list1 + list2
# print(c)

# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# c = list1 + list2
# d = sum(c)
# print(d) 

# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# c = list1 + list2
# d = 0
# for x in c:
#     d = d + x
# print(d)


# nums = input()
# list_ = nums.split(',')
# list_ = sorted(list_)
# print(list_)

# a = [float(input()) for i in range(3)]

# if len(set(a)) == len(a):

#    print("ERROR")

# else:

#    print("YES")



# list_ = [1,2,3]
# for x in list_:
#     x == 1
#     print('Yes')
# else:
    
#    print('ERROR')




# list_ = [1,2,3] 
# set_ = set(list_) 
# if len(set_) != len(list_): 
#    print('yes') 
# else: 
#    print('ERROR')


# list_ = []
# for x in range(54, 9184):
#    if x % 5 == 0:
#       list_.append(x)

# print(list_)



# list_ = [20, 10, 20, 1, 100] 
# list_.sort() 
# min_number = list_[0] 
# print(min_number)


# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = []
# for x in tuples:
#     if x != ():
#         cleared_tuples.append(x)
# print(cleared_tuples)






# name1 = input("Введите имя и фамилию: ") 
# name2 = input("Введите имя и фамилию: ") 
# name3 = input("Введите имя и фамилию: ") 
# name4 = input("Введите имя и фамилию: ") 
# name5 = input("Введите имя и фамилию: ") 
# list1 = name1.split()
# list2 = name2.split()
# list3 = name3.split()
# list4 = name4.split()
# list5 = name5.split()
# sring1 = list1[-1] + ' ' + list2[-1] + ' ' + list3[-1] + ' ' + list4[-1] + ' ' + list5[-1]
# total_list = sring1.split()
# print(sorted(total_list))


# list_ = [] 
# name1 = input("Введите имя и фамилию: ") 
# name2 = input("Введите имя и фамилию: ") 
# name3 = input("Введите имя и фамилию: ") 
# name4 = input("Введите имя и фамилию: ") 
# name5 = input("Введите имя и фамилию: ") 
# list_.append(name1) 
# list_.append(name2) 
# list_.append(name3) 
# list_.append(name4) 
# list_.append(name5) 
# target = " " 
# surnames = [] 
# for x in list_: 
#    t = x.find(target) 
#    v = x.rfind(target) 
#    if x.count(target) > 1: 
#       surnames.append(x[v+1:]) 
#    else: 
#       surnames.append(x[t+1:]) 
      
# print(sorted(surnames))






     
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# count = 0
# x = 8
# for y in list_:
#     if y == x:
#         count += 1
# print(count)


# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# count = []
# x = 8
# for y in list_:
#     if y == x:
#         count.append(y)
# print(len(count))

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]



# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# c = list1 + list2
# d = sum(c)
# print(d) 

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# sum_ = 0
# for x in list_:
#     if type(x) == int:
#         sum_ = sum_ + x 
#     elif x.isdigit(): # переделал строку в int
#         sum_ = sum_ + int(x)

# print(sum_)

# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# for x in str_list:
#     if x[0] == x[-1]:
#         indexs.append(str_list.index(x))
# print(indexs)















# def isEven(num: int) -> bool:
#     """Our function return True or False ehile checking number for even number"""

#     return True if num % 2 == 0 else False

# print(isEven(5))
# print(isEven(6))





# try:
#     n = int(input('Vvedite chislo'))
# except ValueError:
#     print('Invalid number!')
# else:
#     dict_ = {x: x ** 2 for x in range(1, 501) if x % n == 0}
#     print(dict_)


# dict_ = {'Murat': 24, 'Erjan': 21, 'Karina': 24, 'Altynai': 17, 'Aibek': 16}

# for x in dict_:
#     if dict_[x] > 17:
#         print(f'{x} proshel!')
#     else:
#         print(f'{x} ne proshel!')



































