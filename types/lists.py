# list() -> (списки, масив) - изменяемый, последовательный тип данных,
 # который представляет из себя коллекцию каких либо объектов(значения).

# my_list = [1 , 'string', False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))

# range()- возвращает последовательность элементов(чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)
# list()


# my_list = list('Hello world')
# print(my_list)
# ls = ['hello world']
# print(ls)


# tuple_ = ('banana', 'aplle', 'cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))


# Индексация в списках 
# ls = [1,2,3,4,5, 'string', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:]) # [


# ls = [1,2,3,4,5, 'string', [True, False, None], 4,5,6]
# print(ls[6][2])


# for 

# i = 0
# while i < 5
#     print(i)
#     i += 1


# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print(num)

# ls = ['John', 'Sansa', 'Tririon', 'Eddar', 'Serseya', 'Jamie']
# print(ls, len(ls))
# for x in ls[1:]:
#     if x == 'Eddar':
#         print(f"Hello  mr/mrs {x}! Welcome to the pathy")
#         print(x)

# print('2')




# задача на уроке
# ls = list(range(1, 21))
# print(ls)
# for num in ls:
#     if num % 2 == 0:
#         print(f'Число чётное,{num}, квадрат: {num**2}')
#     else:
#         print(f'Число нечётное {num}, куб: {num**3}')


#-------------------------------------------------------------------------------------------------------------------

# методы списков

# print(dir([]))

#append(element) - Добавляет элемент в конце списка

# ls = [1,2,3] 
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True, False])
# print(ls)


#extend(object) - расширяет список
# ls = [1,2,3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# ls.extend(str(56))
# ls.extend([1,2,3])
# print(ls)

# ls = [1,2,3]
# ls1 = [4,5,6]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse = True, 
# то список отсортируется в убывающем порядке


# from random import randint
# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort(reverse=True)
# print('After:')
# print(ls)



# ls = ['John', 'Deyneris', 'Triton', 'Aizirek']
# ls.sort(key=len, reverse=True)
# print(ls)


# insert(index, element) - добавляет элемент по указаному index

# ls = ['string', 2, 3, False]
# ls.insert(1, 1)
# print(ls)



# remove(element) - удоляет element из списка, если такого нет, то выводится ошибка 
# pop([index]) - удоляет и возвращает элемент из списка по index, 
# но если index не передавать, то удаляет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# # ls.remove(5)
# # print(ls)
# # print(5 in ls)
# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [5, 1, 2, 3, 4, 5, 5]
# # print(ls.pop(3))
# # print(ls.remove(5)) # None
# deleted = ls.pop()
# print(deleted)
# print(ls)

# update --------------------------------------------------------------

# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'forth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)




# positiv = int(5)
# negativ = int(-5)
# print(abs(positiv))
# print(abs(negativ))





# name = 'John'
# print(f'I\'m {name}')


# a = int(input('Vvidite imya:'))
# print(a)








# print("Ноль в качестве знака операции"
#       "\nзавершит работу программы")
# while True:
#     s = input("Знак (+,-,*,/): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print("%.2f" % (x+y))
#         elif s == '-':
#             print("%.2f" % (x-y))
#         elif s == '*':
#             print("%.2f" % (x*y))
#         elif s == '/':
#             if y != 0:
#                 print("%.2f" % (x/y))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")




# x=float(input("Введите значение x ="))   
# y=float(input("Введите значение y ="))   
# z=input("Введите оператор (+, -, /, *, mod, pow, div) =")   
# if z==+:      
#     result=x+y   
# elif z==-:     
#     result=x-y   
# elif z==pow:     
#     result=pow(x,y)   
# elif z==*:      
#     result=x*y    
# elif y!=0:     
#     if z==/:       
#     result=x/y     
# elif z==div:        
#     result=x//y     
# elif z==mod:        
#     result=x%y      
# elif y==0:      
#     result="Деление на 0!"   
#     print("Результат вычислений =",result)




















































