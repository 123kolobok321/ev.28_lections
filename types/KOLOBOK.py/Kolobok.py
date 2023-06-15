# res = []
# size = 3
# for i in range(1, size+1):
#     grid = []
#     for j in range(1, size+1):
#         grid.append(j)
#     res.append(grid)
# print(res)




# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists,key=len)
# min_list = min(lists, key=len)
# print(max_list, min_list)
# print(min(lists))



# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_ = max([x for x in lists], key=len) 
# min_ = None 
# if len(lists) > 1: 
#     min_ = min([x for x in lists], key=len) 
# if max_ == min_: 
#     min_ = None 

# print(f'max_list {max_}') 
# print(f'min_list {min_}')



# ls = list(range(1, 11))
# print(ls)

# for t in range()




# n = int(input()) 
# if n >= 11 and n <= 14: 
#     print(f'На лугу пасется {n} коров') 
# else: temp = n % 10 
# if temp == 0 or (temp >= 5 and temp <= 9): 
#     print(f'На лугу пасется {n} коров') 
# if temp == 1: 
#         print(f'На лугу пасется {n} корова') 
# if temp >=2 and temp <=4: 
#     print(f'На лугу пасется {n} коровы')

# labels = ['Honda', 'Kawasaki']
# for x in labels:
#     if labels.()






# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# later = input()
# slovo = []
# for x in list_:
#     if later == x[0]:
#         slovo.append(x)
# print(slovo) 



# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list2 = []
# for x in list_:
#     list2 = range(len(list_))[: step]
# print(list2)

# step = 3 
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] 
# list1 = [list_[i::step] for i in range(len(list_))][:step] 
# print(list1)

# step = 3 
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'] 
# list1 = [list_[i::step] for i in range(len(list_)) if i < step] 
# print(list1)






# step = 3 
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []
# for x in range(len(list_)):
#     if x < step:
#         list1.append(list_[x::step])

# print(list1)


# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# for x in colors1.copy():
#     if x in colors2.copy():
#         colors2.remove(x)
#         colors1.remove(x)

# print(f'{colors1}\n{colors2}')

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# str1 = [x for x in colors1 if not x in colors2]
# str2 = [y for y in colors2 if not y in colors1]
# # for x in colors1:
# #     if not x in colors2:
# #         str1.append(x)

# # for y in colors2:
# #     if not y in colors1:
# #         str2.append(y)       
# print(str1,str2)


# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# flag = False
# for x in list1:
#    if x in list2:
#       flag = True

# if flag == True:
#    print(True)
# else:
#    print(False)

# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for x in list_:
#     if list_.count(x) >= repeats and not x in res:
#         res.append(x)
        
# print(res)
        
# from itertools import permutations
# list_ = [1, 2, 3]
# combinat = permutations(list_)
# for x in combinat:

#     print(x)

# print(combinat)


# K = 3 
# list1 = [] 
# ls = [0] 
# for i in range(K): 
#     list1.insert(i, ls * K) 
# print(list1)



# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# colors.sort(key=len)
# newcolors = []
# for x in colors:
#     newcolors.append(x[::-1])
    
# print(newcolors)

# a = [1,2,3,4,5]
# a.append(6)
# print(a)

# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# i = step
# while i < len(list_) + 1:
#     list_.insert(i, element)
#     i += step + 1

# print(list_)

# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# lists.sort(key=sum)

# print(lists[-1])



# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeats = 2
# repeated = []
# for x in list_:
#     if list_.count(x) >= repeats and not x in repeated:
#         repeated.append(x)

# print(repeated)

# repeated = [20, 30, -20, 60]



# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# chars_str= []
# chars_list = []
# for x in chars:
#     if chars.index(x) >= chars.index(merge_from) and chars.index(x) <= chars.index(merge_to):
#         chars_str.append(x)
#     else:
#         chars_list.append(x)
    

# str_ = ''.join(chars_str)
# chars_list.insert(chars.index(merge_from), str_)

# print(chars_list)


# a = {'apple': 2, 'orange': 5, 'banana': 10}
# for k,v in a.copy().items():
#     if v % 2 == 0:
#         a.pop(k)

# print(a)


# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = {k: v for k, v in a.items() if v % 2 != 0}
# print(b)


# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()): 
#     if v % 2 == 0: 
#         del a[k] 
        
# print(a)


# a = {'a': 1, 'b': 2, 'c': 3} 
# b = a.copy()
# for k,v in a:
#     if k.replace(k,v):

#         print(a)
            
# dict(reversed(item) for item in e2f.items())

# a = {'key': 'val'}
# a = {'a': 1, 'b': 2, 'c': 3} 
# res = {v: k for k, v in a.items()}
# print(res)

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)



# if __name__ == '__main__':
 
#     d = {'A': 1, 'B': 2, 'C': 3}
#     total = sum(d.values())
 
#     print(total)

# name = ('John', 'Nicholas', 'Mercy') 
# age = 25 

# dict_sample = dict.fromkeys(name, age) 

# print(dict_sample)

# name = ('John', 'Nicholas', 'Mercy')

# dict_sample = dict.fromkeys(name) 

# print(dict_sample)
# dict_sample = {
#   "Company": "Toyota", 
#   "model": "Premio", 
#   "year": 2012 
# } 

# x = dict_sample.setdefault("color", "Gray") 
# print(x)


# a1 = {"a": 1,"b": 2,"v": 3} 
# a2 = dict(a=1, b=2, c=3) 
# # a3 = {} 
# # for k,v in a1.items(): 
# #     a3.setdefault(k, v) 
# #     print(a1) 
# #     print(a2) 
# #     print(a3)
# a4 = {k: k * 2 for k in range(1, 10)}
# print(a4)
# print(a1) 
# print(a2) 

# a1 = {"a": 1,"b": 2,"v": 3} 
# a2 = dict(a=1, b=2, c=3) 
# a3 = {k: v * 2 for k, v in a1.items()}
# print(a3)
# print(a1) 
# print(a2) 

# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('x'))

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['b']
# print(dict_)

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# dict1 = {k: v for k, v  in dict_.items() if k != 'a'}
# print(dict1)
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# dict_ = {k: v for k, v  in dict_.items() if k != 'a'}
# print(dict_)



# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)

#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# переменная в foo:  переменная foo
# переменная в foo:  переменная bar

# x = 'Я глобальная переменная!'
# def my_func():
#     global x 
#     print(x)
#     x = 'Я могу изменяться'
#     return x 

# my_func()
# print(x)

# num = 3
# def mul():
#     global num
#     num = num ** 2

# mul()
# mul()
# mul()
# print(num)


# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')
    

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result = 0
# def pow_first(x,y):
#     global result
#     result = x ** y 
    


# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# for x in a:
#     if a[x] >= 17:
#         print(f'{x}, Вы можете войти в клуб')
#     else:
#         print(f'{x}, извините, Вы не проходите по age-control')


# Мурат, Вы можете войти в клуб
# Эржан, Вы можете войти в клуб
# Чынгыз, Вы можете войти в клуб
# Алтынай, Вы можете войти в клуб
# Асема, извините, Вы не проходите по age-control

# a = ['pipi', 'papa', 'mama']
# b = []
# for x in a:
#     b.append(x.capitalize())

# print(b)
        
      
# def count_symbols(str_):
#     glass = 0
#     sogls = 0
#     symb = 0
#     for x in str_:
#         if x in 'аиоуыэ':
#             glass += 1
#         elif x in 'йклмнпрстфхцчшщ':
#             sogls +=1
#         else:
#             symb += 1

# print(count_symbols)
    
    
# def count_symbols(str_):
#     glass = 0
#     sogls = 0
#     symb = 0
#     for x in str_:
#         if x.lower() in 'аяуюоеёэиы':
#             glass += 1
#         elif x.lower() in 'бвгджзйклмнпрстфхцчшщ':
#             sogls +=1
#         else:
#             symb += 1
    
#     return f'Количество гласных: {glass}, согласных: {sogls}, остальных символов: {symb}'

# print(count_symbols('Мурат супер!'))
    
    
# a = [x for x in range(0, 11)]
# print(a)


# a=[] 
# def func(): 
#     global a 
#     a=[i for i in range(0,11)] 

# print(func()) 


# list_ = [1, 2, 3, 4, 5]
# new_list = ['нечетное' if x % 2 != 0 else 'четное' for x in list_]
# print(new_list)

# a = {'hello', 'world', '21'}
# print(len(a))


# a = {'Jane', 'Eyre', 22}
# a.add('Hello world!')
# print(a)

# a = {1,2,3}
# b = {3,4}
# a.update(b)
# print(a)


# a = {1,2,3}
# a.discard(4)
# print(a)

# a = {1,2,3}
# a.remove(4)
# print(a)


# a = {1,False,3}
# a.clear()
# print(a)

# a = {4, 6, 100, -45, -6} 
# b = {4, 5, -5, -6}
# print(a & b)


# a = {4, 6, 100, -45, -6} 
# b = {4, 5, -5, -6}
# print(a | b)


# list_ = [item for item in range(1, 101)]    
# print(list_) 

# list_ = [i for i in range(1,51) if i % 2 != 0] 
# print(list_)


# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x x % 2 = 0 for x in list_ if x > 0]
# print(int_list)




# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x for x in list_ if x % 2 == 0 and x > 0]
# print(int_list)

# import functools 

# # my_list =  ['m', 'a', 'k', 'e', 'r', 's'] 
# list_ = [1, 2, 3, 4] 
# result = functools.reduce(lambda x, y: x + y, list_) 
# print(result) 

# list_ = [1, 2, 3, 4] 
# result = sum(list_)
# print(result)


# list1 = ['THIS', 'IS', 'SOME','LIST']
# new_list1 = all(str.isupper() for str in list1) 
# print(new_list1) 


# list_ = [5, 8, 4, 6, 7] 
# result = all(x > 3 for x in list_) 
# print(result) 

# list1 = ['some', 'string', '42'] 
# new_list1 = any(str.isdigit() for str in list1) 
# print(new_list1) 


# list_ = [5, 8, 4, 6, 7, -99]
# result = any(x < 0 for x in list_)
# print(result)


# def virus_count(hours: int):
#     amount = 1
#     bac = 0
#     for min in range(hours * 60 + 1):
#         if bac >= 100:
#             amount += 1
#             bac = bac % 100
#         bac += 4 * amount
#     return amount

# print(virus_count(999))



# nums = [1, 2, 3, 4, 5, 6, 7] 
# map(lambda x: x ** 3, nums) 
# new_nums = list(map(lambda x: x ** 3, nums)) 
# print(new_nums)

# list_ = [1, 2, 3, 4, 5, 6, 7] 
# result = list(map(lambda x: x + 2, list_))
# print(result)


# fruits = ['apple', 'banana', 'grapes', 'apricot'] 

# a_words = list(filter(lambda word : word.startswith('a') , fruits))  
# print(a_words) 


# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0 in list_))
# print(result)


# num = 9, 4
# def sum_one(num):
#   result = result + num
# print(num)

# list_ = [1,2,3,4,5]
# new_list = [x: x ** 2 for x in list_]
# print(new_list)

# num = 9, 4
# def sum_one(num):
#   result = result + num
# print(num)



# nums = [1, 2, 3, 4, 5]
# new_nums = [item ** 3 for item in nums] 
# print(new_nums) 


# list_ = [i ** 2 for i in range(1, 26)]
# print(list_)


# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)

# try: 
#     pass 
# except:
#     pass 
# else: 
#     pass 
# finally:
#     pass

# def mul():
#     def mul(x, z):
#         def mul(x, z): 
#             x * z
# def mul(x, z):      
#  return x * z  
# print(mul(2,3))  


# def add(num1 , num2):
#     return num1 + num2 
# print(add(99, 9998))


# def get_string_length(str):
#     return  len(str)
# print(get_string_length('World of Tanks')) 

# fruits = ['apple', 'banana', 'grapes', 'apricot']
# a_words = list(filter(lambda word : word.startswith('a') , fruits))  
# print(a_words)

# from functools import reduce
# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x : x % 2 == 0, list_))
# print(result)
####from functools import reduce
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x : len(x) > 7, list_))
# print(result)

# list_ = [1, 2, 3, 4] 

# try: 
#     print(list_[3]) 
# except IndexError: 
#     print("такого индекса не существует") 
# except: 
#     print("что-то пошло не так")



# try:
#     b = 10
#     c = 11

#     print(a)
# except:
#     print('Такой переменной не существует!')


# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1/num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(result)


# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(result)

####МАТРЁШКА####

# matr = 10

# def size_matr():
#     matr2 = 5
   
#     def size_matr2():
#         matr3 = 3

#         return matr3 + matr2
    
#     return size_matr2() + matr
        
# print(size_matr())


# nums = [13,25,83,77]

# def separateDigits(self, nums: List[int]) -> List[int]:
#         res =[]
#         for i in nums:
#             res.extend(map(int,str(i)))
#         return res


#    def separateDigits(self, nums: List[int]) -> List[int]:
#         res =[]
#         for i in nums:
#             res.extend(map(int,str(i)))
#         return res


# pos = 0
#         neg = 0
#         for i in nums:
#             if i > 0:
#                 pos +=1
#             elif i < 0:
#                 neg +=1
#         return max(pos,neg)


# list_ = [
#     'hello',
#     6, 
#     [1,2,3]
# ]

# num = 2

# def collect_all_possibles(list_: list, num: int) -> list:
#     res = []
#     for i in list_:
#         try:
#             res.append(i + num)
#         except:
#             pass
#         try:
#             res.append(i - num)
#         except:
#             pass
#         try:
#             res.append(i * num)
#         except:
#             pass
#         try:
#             res.append(i ** num)
#         except:
#             pass
#         try:
#             res.append(i // num)
#         except:
#             pass
#     return res

# a = collect_all_possibles(list_, num)
# print(a)

# dict_ = {'key1': 'value1', 'key2': 'value2'}






# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try: 
#     print(dict_['key1']) 
# except KeyError: 
#     print('Нет такого ключа!')


# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     list_.index()
# except 


# a = {2, 4, 6, 50, -45, -6}
# b = {4, 3, 5, -5, -6}
# print(a.difference(b))


# a = {2,4,6,50,-45,-6} 
# b = {4,3,5,-5,-6} 
# print(a - b)

# a = {0, 1, 2} 
# b = {0, 1, 2, 3, 34, 5, 8, 13}
# # print(a.issubset(b))
# if a.issubset(b) == True:
#     print('Подмножество!')

# a = {0, 1, 2, 3, 34, 5, 8, 13} 
# b = {1, 2, 34}
# if b.issubset(a):
#     print('Надмножество!')


# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}
# if robert.intersection(kail) and robert.intersection(merri):
#     print("kail merri")
# elif robert.intersection(kail):
#     print('kail')
# elif robert.intersection(merri):
#     print('merri')
# else:
#     print('no one')



# a=set(["Вася","Петя"])
# b=set(["Петя","Оля"])
# c=a.intersection(b)
# d=a.union(b)
# print(c)
# print(d)

# tilek = {"Dodo","ImperiaPizza","FreshBox"}
# timur = {"OchakKebab", "FreshBox"}
# alexander = {"FreshBox", "KFC"} 
# elina = {"Dodo","ImperiaPizza","FreshBox", "OchakKebab", "KFC"}

# choice = tilek&timur&alexander&elina  
# print(choice) 

# list_ = range(1, 11)
# list_ = [x ** 2 if x % 2 == 0 else x for x in list_]
# print(list_)

# list_ = range(1,11)
# list_ = [True if x % 2 == 0 else False for x in list_]
# print(list_)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name]
# print(new_list)


# dict_ = {num : num ** 2 for num in range(1, 10)} 
# print(dict_) 

# n = int(input()) 
# dict_ = {x : x**2 for x in range (1, 501) if x % n == 0} 
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {x: [i for i in range(1, y+1)] for x,y  in a.items()}
# print(dict_)

 
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()}
# a = {k:'evin' if v%2==0 else 'odd' for k,v in dict_.items()}
# print(a)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'odd' if v % 2 != 0 else 'even' for k, v in dict_.items()} 
# print(a)





# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [x for x in string_.split() if x.isdigit()]
# print(list_)



# with open('task2.txt', 'r') as file:  
#     for line in file.readlines():
#         print(line)
        



# with open('task1.txt', 'r') as file:  
#     file.readlines(13)
#     print(file)



# with open('task2.txt', 'r') as file: 
#     for l in file.readlines(): 
#         print(l)



# with open('task3.txt','w+') as file:
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0)
#     print(file.read())



# with open('task4.txt','r') as file:
#     print(len(file.readlines()))


# with open('task5.txt', 'r') as f: 
#     list_ = [] 
#     ful = f.read() 
# for i in ful.split(): list_.append(int(i)) 
# with open('task6.txt', 'x') as fw: 
#     fw.write(f'{min(list_)}-{max(list_)}') 


# with open('task5.txt', 'r') as f: 
#     list_ = f.readlines() 
#     list_ = [line.replace('\n', '')for line in list_] 
#     list1 = [] 
#     for i in list_: 
#         i = int(i) 
#     list1.append(i) 
# a = min(list1) 
# b = max(list1) 
# with open('task6.txt', 'w') as fw: 
#     fw.write(f'{a}-{b}')


# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict={x:max(y,key=lambda x:y.get(x)) for x,y in dict_.items()} 
# print(new_dict)



# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:y for k,v in my_dict.items() for x,y in v.items()} 
# print(dict_)



# list_= [x for x in range(1, 26) if x % 2 == 0]
# print(list_)


# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x if x >= 0 else 1 for x in list_]
# print(int_list)

# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [x for x in list1 if type(x) == str]
# print(list2)

# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x > 5]
# print(list1)

# list_ = [False, True, False, True, False, True, False, True, False, True]
# list_ = [1 if x == True else 0 for x in list_]
# print(list_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = [len(x) for x in list_name ]
# print(new_list)


# list_ = range(1, 1001, 125)
# new_list = [x for x in list_ if x % 2 == 0]
# print(new_list)

# list1 = [44,54,64,74,104]
# list2 = [x + 6 for x in list1]
# print(list2)


# list1 = [2, 4, 6, 8, 10, 12, 14]
# list2 = [x for x in list1 if x**2 > 50]
# print(list2)



# string = "happy birthday!"
# list1 = list(string)
# list_ = [x for x in string if x != ' ' and x != '!']
# print(list_)


# string = "happy birthday!"
# list_ = [list(x) for x in string if x != '' and x != '!']
# print(list_)

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list1 = [v for k,v in dict_.items() for x,v in v.items()]
# print(list1)



# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} 
# list1 = [y for k,v in dict_.items() for x,y in v.items()] 
# print(list1)





# list_ = [1, 4, 9, 16, 25, 36] 
# try: 
#     print(list_[5]) 

# except: print('Такого элемента нет!!!')


# x = 5  
# try: 
#   print(x) 
# except: 
#   print("что-то пошло не так") 
# else: 
#   print("ошибок не возникло") 
# finally: 
#   print("'try except' закончил свою работу") 


# try: 
#     age = int(input()) 
#     if age < 18: 
#         raise ValueError('Доступ запрещён') 
# except: 

#     print('Введён некорректный возраст') 
    
# else:   
#     print('Спасибо') 
# finally: 
#     print('До свидания!')


# try: 
#     num1 = int(input()) 
#     num2 = int(input()) 
#     res = num1 / num2 
# except (ValueError, ZeroDivisionError): 
#     print('Произошла ошибка!') 
# else:
#     print(res)

# import json  
# with open('file.json', 'r') as f: 
#     result = json.loads(f.read()) 
#     print(result)



# import json 
# file1 = open('task1.json') 
# python_obj = json.loads(file1.read()) 
# file1.close() 
# with open('task1.py', 'w') as file2: 
#     file2.write(str(python_obj))





# from functools import reduce 
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x, y: x * y, list_) 
# print(result)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_))) 
# list3 = len(list(filter(lambda x: not x % 2 == 0, list_))) 
# result = f'even: {list2}, odd: {list3}' 
# print(result)


# def get_type(a,b): 
#     print(f'{type(a)}\n{type(b)}') 
# get_type(99,'999')



# number = 8
# string = 'kolobok'
# res = number * string
# print(res)


# positive = 5
# negative = -5
# print(abs(positive))
# print(abs(negative))


# x = 90
# print(pow(90,3))


# num1 = int(input())
# num2 = int(input())
# num3 = 2.5
# print((num1 % num2) * num3)

# decimal = 10.0
# print(decimal**2)
# print(decimal**3)
# print(decimal**0.5)

# стороны треугольника
# from math import sqrt 
# leg_a = 3 
# leg_b = 4 
# hypotenuse = sqrt(leg_a ** 2 + leg_b ** 2) 
# print(hypotenuse)


## TELEGRAMBOT


# import telebot 
# from telebot import types
# import random

# token = '6052003708:AAEeHvI7b05-YQnlRj2oWA_Y-UEOKF9-P_E'

# bot = telebot.TeleBot(token)

# keyboard = types.ReplyKeyboardMarkup()
# button1 = types.KeyboardButton('Играть')
# button2 = types.KeyboardButton('Нет')

# keyboard.add(button1, button2)

# @bot.message_handler(commands=['start', 'game'])
# def start_message(message):
#   message2 = bot.send_message(message.chat.id, 'Привет, начнем игру?', reply_markup=keyboard)
#   bot.register_next_step_handler(message2, check_answer)

# def check_answer(message):
#   if message.text == 'Играть':
#     bot.send_message(message.chat.id, 'Хорошо, тогда вот правила, нужно угадать число за 3 попытки')
#     random_number = random.choice(range(1, 11))
#     print(random_number)
#     game(message, 3, random_number)
#   else:
#     bot.send_message(message.chat.id, 'Пока')

# def game(message, attempts, random_number):
#   message2 = bot.send_message(message.chat.id, 'Введи число')
#   bot.register_next_step_handler(message2, check_number, attempts-1, random_number)
  
# def check_number(message, attempts, random_number):
#   if message.text == str(random_number):
#     bot.send_message(message.chat.id, 'Вы победили')
#   elif attempts == 0:
#     bot.send_message(message.chat.id, 'Извините, у вас закончились попытки')
#   else:
#     bot.send_message(message.chat.id, 'Попробуйте еще раз')
#     game(message, attempts, random_number)

# bot.polling()


# string = 'string'
# print(string[::-1])

# string1 = 'makers'
# string2 = 'bootcamp'
# print(string1 + ' ' + string2)

# string = 'hey'
# print(string * 4)


# string = 'world'
# print(len(string))

# my_str = 'Сегодня четверг' 
# new_str = my_str.replace('четверг', 'пятница') 
# print(new_str)


# string = 'The quick brown fox jumps over the lazy dog'
# str1 = string.replace('o', '*')
# print(str1)

# my_str = 'Ла Ла Лэнд' 
# print(my_str.count('Л')) 

# string = 'kolobok'
# print(string.upper())

# string = 'БЕГИ ФОРЕСТ, БЕГИ!'
# print(string.lower())



# import json 
# with open("task2.json","r") as file: 
#     json_obj = file.read() 
#     python_obj = json.loads(json_obj) 
#     print(json_obj)


# def message_add():
#     with open('text.txt') as file:
#         list_ = file.read()
        




# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# res = {name: len(name) ** 2  for name in list_name if len(name) > 4}
# print(res)


# import json 
# def bulk_create(products): 
#     with open('db.json') as f: 
#     old = json.load(f) 
#     id_ = [i['id'] for i in old] 
#     for el in products: 
#         if el['id'] not in id_: old.append(el) 
#         with open('new_db.json', 'w') as f2: 
#             json.dump(old, f2) 
# bulk_create([{'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}])

####Parsing Neznau chto eto
# from bs4 import BeautifulSoup 
# import requests 
# import csv 
# source = requests.get('https://stackoverflow.com/questions').status_code 
# print(f'source = {source}')



# string = 'hello' 
# print (string[-1] + string[1:-1] + string[0])


# string = 'Hello'
# print(string[::-1])


# hashtags = '#makers#bootcamp#программирование#it#курсы'
# print(hashtags.lstrip('#').split('#'))

# name = input()
# last_name = input()
# age = input()
# city = input()
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')


# string = 'Makers bootcamp'
# print(string[1::2])

# string = 'abracadabra'
# print(string[:5]+'K'+ string[6:])


# list_ = [-1, 2, 3, 5, -3, 7]
# result = list(map(lambda x: True if x > 0 else False, list_))
# print(result)




# import requests 
# source = requests.get('https://stackoverflow.com/questions').status_code
# # source = url.status_code
# print(source)


# from bs4 
# import BeautifulSoup 
# import requests 
# import csv 
# source = requests.get('https://stackoverflow.com/questions').status_code 
# print(source)


# from bs4 import BeautifulSoup 
# import requests 
# import lxml
# source = requests.get('http://www.example.com/').text 
# my_page = BeautifulSoup(source, 'lxml')
# print('h1:', my_page.h1.text) 
# print('p:', my_page.p.text) 
# print('a:', my_page.a.get('href')) 




# from bs4 import BeautifulSoup
# import requests
# import lxml

# source = requests.get('https://wikipedia.org/').text 
# my_page = BeautifulSoup(source, 'lxml')
# a = my_page.find('div', class_ = 'central-featured-lang lang4').find('a')
# lang = a.find('strong').text
# num = a.find('small').find('bdi').text
# artik = a.find('small').find('span').text

# print(lang)
# print(num, artik)



# def getTitle(url):
#     from bs4 import BeautifulSoup
#     import requests
#     import lxml
#     source = requests.get(url).text
#     my_page = BeautifulSoup(source,'lxml')
#     if my_page('h1'):
#         return my_page('h1')
#     else:
#         return "Title could not be found"
        
# print(getTitle('http://www.example.com/'))



# from bs4 import BeautifulSoup
# import requests

# response = requests.get('https://www.imdb.com/chart/top').text
# soup = BeautifulSoup(response, 'lxml')
# container = soup.find('div', class_='lister').find('table', class_='chart full-width').find('tbody', class_='lister-list')
# films = container.find_all('tr')
# title_list = []
# for item in films:
#     film_link = 'https://www.imdb.com' + item.find('td', class_='titleColumn').find('a').get('href')
#     film_name = item.find('td', class_='titleColumn').find('a').text
#     data = {'name': film_name, 'link': film_link}
#     title_list.append(data)

# def get_link(title_list, name):
#     for i in title_list:
#         if name.lower() in i['name'].lower():
#             return i['link']
    

# print(get_link(title_list, 'shawshank'))


#





# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# res = {name: len(name) ** 2  for name in list_name if len(name) > 4}
# print(res)


# from functools import reduce 

# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_) 
# print(result)


# def num_kol():
#     result = ['Fizz' if x % 3 == 0 else 'Buzz' for x in range(1, 51)]
#     return result

# print(num_kol())


# from functools import reduce 
# list_=list(range(1,50)) 
# result = list(map(lambda x: 'Fizz' if x % 3 == 0 else 'Buzz', list_)) 
# print(result)


# import csv
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# from multiprocessing import Pool

# def get_html(url: str) -> str:
#     '''Эта функция получает HTML разметку по определенному сайту по URL'''
#     response = requests.get(url)
#     return response.text

# def get_soup(html: str) -> BeautifulSoup:
#     ''' Получает html разметку и структурирует ее в красивый bs'''
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def get_all_links():
#     res = []
#     i = 1
#     while True:
#         url = f'https://www.mashina.kg/search/all/?page={i}'
#         res.append(url)
#         print(url)
#         if i == 1749:
#             break
#         i += 1
#     return res

# def get_data(link: BeautifulSoup) -> list:
#     html = get_html(link)
#     soup = get_soup(html)
#     '''Получает нужные данные с сайта машина кджи'''
#     container = soup.find('div', class_='table-view-list')
#     cars = container.find_all('div', class_='list-item')
#     result = []
#     for car in cars:
#         name = car.find('h2', class_='name').text.strip()
#         try:
#             img = car.find('img', class_='lazy-image').get('data-src')
#         except:
#             img = 'No image'
#         price_div = car.find('div', class_='block price')
#         price = price_div.find('p').find('strong').text
#         ls = ['year-miles', 'body-type', 'volume']
#         desc = ', '.join(car.find('p', class_=x).text.strip() for x in ls)
#         data = {
#             'name': name,
#             'desc': desc,
#             'price': price,
#             'img': img
#         }
#         result.append(data)
#     return result

# def prepare_csv() -> None:
#     '''Функция, которя подготавливает csv файл!'''
#     with open('cars.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow([
#             'Name',
#             'Description',
#             'Price',
#             'Image URL'
#         ])

# def write_to_csv(data: list) -> None:
#     '''Записывает все данные в csv файл'''
#     with open('cars.csv', 'a') as file:
#         fieldnames = ['Name', 'Description', 'Price', 'Image URL']
#         writer = csv.DictWriter(file, fieldnames) 
#         for car in data:
#             writer.writerow({
#             'Name': car['name'],
#             'Description': car['desc'],
#             'Price': car['price'],
#             'Image URL': car['img']
#             }) 

# def make_all(link):#8
#         data = get_data(link)
#         write_to_csv(data)        


# def main():
#     prepare_csv()
#     links = get_all_links()
#     with Pool(40) as pool:
#         pool.map(make_all, links)


# if __name__ == '__main__':
#     start = datetime.now()
#     main()
#     finish = datetime.now()
#     print(f'Parsing takes: {finish - start} time')











# 1)	В текстовом файле посчитать количество строк, а также для каждой отдельной строки определить количество в ней символов и слов.


# from bs4 import BeautifulSoup
# import requests
# import lxml


# 'gkInnerInsetLeft'

# def get_html(url: str) -> str:
#     '''Эта функция получает HTML разметку по определенному сайту по URL'''
#     response = requests.get(url)
#     return response.text


# def get_soup(html: str) -> BeautifulSoup:
#     ''' Получает html разметку и структурирует ее в красивый bs'''
#     soup = BeautifulSoup(html, 'lxml')
#     return soup


# def get_all_links():
#     res = []
#     i = 1
#     while True:
#         url = f'https://vesti.kg/'
#         res.append(url)
#         print(url)
#         if i == 1:
#             break
#         i += 1
#     return res









# from bs4 import BeautifulSoup
# import requests

# response = requests.get('https://vesti.kg/').text
# soup = BeautifulSoup(response, 'lxml')
# container = soup.find('section', class_='gkMainbody').find('div', class_='gkInnerInsetLeft')
# novosti = container.find_all('div')
# title_list = []
# for item in novosti:
#     novosti= 'https://vesti.kg/' + item.find('', class_='titleColumn').find('a').get('href')
#     film_name = item.find('td', class_='titleColumn').find('a').text
#     data = {'name': film_name, 'link': film_link}
#     title_list.append(data)

# def get_link(title_list, name):
#     for i in title_list:
#         if name.lower() in i['name'].lower():
#             return i['link']
    

# print(get_link(title_list, 'shawshank'))


# from bs4 import BeautifulSoup
# from requests import get
# import csv


# def get_html(url):
#     response = get(url)
#     return response.text

# def get_soup(html):
#     soup = BeautifulSoup(html, 'lxml')
#     return soup

# def get_data(link):
#     html = get_html(link)
#     soup = get_soup(html)
#     div_title = soup.find_all('div', class_='itemBody')
#     data= []
#     for item in div_title:
#         title_ = item.find('a').text.strip()
#         href_ = 'https://vesti.kg/' + item.find('a').get('href')
#         res = {
#             'title': title_,
#             'link': href_
#         }
#         data.append(res)

#     return data

# def prepare_csv():
#     with open('titles.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow([
#                 '№',
#                 'Titles',
#                 'Link'
#             ])
    
# def write_to_csv(data: list) -> None:
#     with open('titles.csv', 'a') as file:
#         fieldnames = ['№', 'Titles', 'Link']
#         writer = csv.DictWriter(file, fieldnames) 
#         count = 1
#         for item in data:
#             writer.writerow({
#             '№' : count,
#             'Titles' : item['title'],
#             'Link' : item['link']
#             })
#             print(f'Parsing {count} title(s)!')
#             count += 1

# def main():
#     prepare_csv()
#     url = 'https://vesti.kg/'
#     data = get_data(url)
#     write_to_csv(data)

# main()





# import logging
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import (
#     Updater,
#     CommandHandler,
#     CallbackQueryHandler,
#     ConversationHandler,
# )

# # Ведение журнала логов
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
# )

# logger = logging.getLogger(__name__)

# # Этапы/состояния разговора
# FIRST, SECOND = range(2)
# # Данные обратного вызова
# ONE, TWO, THREE, FOUR = range(4)


# def start(update, _):
#     """Вызывается по команде `/start`."""
#     # Получаем пользователя, который запустил команду `/start`
#     user = update.message.from_user
#     logger.info("Пользователь %s начал разговор", user.first_name)
#     # Создаем `InlineKeyboard`, где каждая кнопка имеет 
#     # отображаемый текст и строку `callback_data`
#     # Клавиатура - это список строк кнопок, где каждая строка, 
#     # в свою очередь, является списком `[[...]]`
#     keyboard = [
#         [
#             InlineKeyboardButton("1", callback_data=str(ONE)),
#             InlineKeyboardButton("2", callback_data=str(TWO)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     # Отправляем сообщение с текстом и добавленной клавиатурой `reply_markup`
#     update.message.reply_text(
#         text="Запустите обработчик, выберите маршрут", reply_markup=reply_markup
#     )
#     # Сообщаем `ConversationHandler`, что сейчас состояние `FIRST`
#     return FIRST


# def start_over(update, _):
#     """Тот же текст и клавиатура, что и при `/start`, но не как новое сообщение"""
#     # Получаем `CallbackQuery` из обновления `update`
#     query = update.callback_query
#     # На запросы обратного вызова необходимо ответить, 
#     # даже если уведомление для пользователя не требуется.
#     # В противном случае у некоторых клиентов могут возникнуть проблемы.
#     query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("1", callback_data=str(ONE)),
#             InlineKeyboardButton("2", callback_data=str(TWO)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#    # Отредактируем сообщение, вызвавшее обратный вызов.
#    # Это создает ощущение интерактивного меню.
#     query.edit_message_text(
#         text="Выберите маршрут", reply_markup=reply_markup
#     )
#     # Сообщаем `ConversationHandler`, что сейчас находимся в состоянии `FIRST`
#     return FIRST


# def one(update, _):
#     """Показ нового выбора кнопок"""
#     query = update.callback_query
#     query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("3", callback_data=str(THREE)),
#             InlineKeyboardButton("4", callback_data=str(FOUR)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     query.edit_message_text(
#         text="Вызов `CallbackQueryHandler`, выберите маршрут", reply_markup=reply_markup
#     )
#     return FIRST


# def two(update, _):
#     """Показ нового выбора кнопок"""
#     query = update.callback_query
#     query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("1", callback_data=str(ONE)),
#             InlineKeyboardButton("3", callback_data=str(THREE)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     query.edit_message_text(
#         text="Второй CallbackQueryHandler", reply_markup=reply_markup
#     )
#     return FIRST


# def three(update, _):
#     """Показ выбора кнопок"""
#     query = update.callback_query
#     query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("Да, сделаем это снова!", callback_data=str(ONE)),
#             InlineKeyboardButton("Нет, с меня хватит ...", callback_data=str(TWO)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     query.edit_message_text(
#         text="Третий CallbackQueryHandler. Начать сначала?", reply_markup=reply_markup
#     )
#     # Переход в состояние разговора `SECOND`
#     return SECOND


# def four(update, _):
#     """Показ выбора кнопок"""
#     query = update.callback_query
#     query.answer()
#     keyboard = [
#         [
#             InlineKeyboardButton("2", callback_data=str(TWO)),
#             InlineKeyboardButton("4", callback_data=str(FOUR)),
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     query.edit_message_text(
#         text="Четвертый CallbackQueryHandler, выберите маршрут", reply_markup=reply_markup
#     )
#     return FIRST


# def end(update, _):
#     """Возвращает `ConversationHandler.END`, который говорит 
#     `ConversationHandler` что разговор окончен"""
#     query = update.callback_query
#     query.answer()
#     query.edit_message_text(text="See you next time!")
#     return ConversationHandler.END


# if __name__ == '__main__':
#     updater = Updater("TOKEN")
#     dispatcher = updater.dispatcher

#     # Настройка обработчика разговоров с состояниями `FIRST` и `SECOND`
#     # Используем параметр `pattern` для передачи `CallbackQueries` с
#     # определенным шаблоном данных соответствующим обработчикам
#     # ^ - означает "начало строки"
#     # $ - означает "конец строки"
#     # Таким образом, паттерн `^ABC$` будет ловить только 'ABC'
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler('start', start)],
#         states={ # словарь состояний разговора, возвращаемых callback функциями
#             FIRST: [
#                 CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
#                 CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
#                 CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
#                 CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
#             ],
#             SECOND: [
#                 CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
#                 CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
#             ],
#         },
#         fallbacks=[CommandHandler('start', start)],
#     )

#     # Добавляем `ConversationHandler` в диспетчер, который
#     # будет использоваться для обработки обновлений
#     dispatcher.add_handler(conv_handler)

#     updater.start_polling()
#     updater.idle()





# import telebot
# from telebot import types # для указание типов
# # import config

# token = '6184082580:AAED8O9jnH6Fjw2QkCDwJ3HAA1qm4n7vis4'

# bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("👋 Поздороваться")
#     btn2 = types.KeyboardButton("❓ Задать вопрос")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(message.from_user), reply_markup=markup)
    
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if(message.text == "👋 Поздороваться"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#     elif(message.text == "❓ Задать вопрос"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Как меня зовут?")
#         btn2 = types.KeyboardButton("Что я могу?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
#     elif(message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")
    
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
    
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("👋 Поздороваться")
#         button2 = types.KeyboardButton("❓ Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

# bot.polling(none_stop=True)


# token = '6184082580:AAED8O9jnH6Fjw2QkCDwJ3HAA1qm4n7vis4'

# bot = telebot.TeleBot(token)
# from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     ContextTypes,
#     ConversationHandler,
#     MessageHandler,
#     filters,
# )

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)

# CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

# reply_keyboard = [
#     ["Age", "Favourite colour"],
#     ["Number of siblings", "Something else..."],
#     ["Done"],
# ]
# markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

# def facts_to_str(user_data: Dict[str, str]) -> str:
#     """Вспомогательная функция для форматирования 
#     собранной информации о пользователе."""
#     facts = [f"{key} - {value}" for key, value in user_data.items()]
#     return "\n".join(facts).join(["\n", "\n"])

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Начvало разговора, просьба ввести данные."""
#     await update.message.reply_text(
#         "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
#         "Why don't you tell me something about yourself?",
#         reply_markup=markup,
#     )
#     return CHOOSING

# async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Запрос информации о выбранном предопределенном выборе."""
#     text = update.message.text
#     context.user_data["choice"] = text
#     await update.message.reply_text(f"Your {text.lower()}? Yes, I would love to hear about that!")
#     return TYPING_REPLY

# async def custom_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Запрос описания пользовательской категории."""
#     await update.message.reply_text(
#         'Alright, please send me the category first, for example "Most impressive skill"'
#     )
#     return TYPING_CHOICE

# async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Store info provided by user and ask for the next category."""
#     user_data = context.user_data
#     text = update.message.text
#     category = user_data["choice"]
#     user_data[category] = text
#     del user_data["choice"]

#     await update.message.reply_text(
#         "Neat! Just so you know, this is what you already told me:"
#         f"{facts_to_str(user_data)}You can tell me more, or change your opinion"
#         " on something.",
#         reply_markup=markup,
#     )
#     return CHOOSING

# async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Вывод собранной информации и завершение разговора."""
#     user_data = context.user_data
#     if "choice" in user_data:
#         del user_data["choice"]

#     await update.message.reply_text(
#         f"I learned these facts about you: {facts_to_str(user_data)}Until next time!",
#         reply_markup=ReplyKeyboardRemove(),
#     )
#     user_data.clear()
#     return ConversationHandler.END


# if __name__ == "__main__":
#     application = Application.builder().token("TOKEN").build()

#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             CHOOSING: [
#                 MessageHandler(
#                     filters.Regex("^(Age|Favourite colour|Number of siblings)$"), regular_choice
#                 ),
#                 MessageHandler(filters.Regex("^Something else...$"), custom_choice),
#             ],
#             TYPING_CHOICE: [
#                 MessageHandler(
#                     filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")), regular_choice
#                 )
#             ],
#             TYPING_REPLY: [
#                 MessageHandler(
#                     filters.TEXT & ~(filters.COMMAND | filters.Regex("^Done$")),
#                     received_information,
#                 )
#             ],
#         },
#         fallbacks=[MessageHandler(filters.Regex("^Done$"), done)],
#     )

#     application.add_handler(conv_handler)
#     # Запуск бота.
#     application.run_polling()





# from bs4 import BeautifulSoup
# from requests import get


# html = get('https://enter.kg/').text
# soup = BeautifulSoup(html, 'html.parser')
# container = soup.find('ul', class_='VMmenu')
# category_list = [x.text for x in container.find_all('a')]

# def find_category(categories, keyword):
#     return [x for x in categories if keyword.lower() in x.lower()]
    
# print(find_category(category_list, 'Ноутбуки'))





# https://docs-python.ru/packages/biblioteka-python-telegram-bot-python/ ## эта ссылка как создать бота по шагам
# desc1 = car.find('p', class_='year-miles').text.strip()
        # desc2 = car.find('p', class_='body-type').text.strip()
        # desc3 = car.find('p', class_='volume').text.strip()
        # description = f'{desc1} {desc2} {desc3}'



# 2) Создайте 3 класса:
# Bird, Animal, Plant
# класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
# каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')

# class Bird:
#     def fly(self):
#        print('я лечу')
    
#     def grow(self):
#        pass
    
#     def sound(self):
#        pass
    
# class Animal:
#     def sound(self):
#        pass
        
#     def run(self):
#        pass
    
#     def grow(self):
#        pass
    
# class Plant:
#    def grow(self):
#       pass
#    def photosynthesize(self):
#       pass
   
# bird = Bird()
# bird.fly()
# bird.grow()
# bird.sound()
# animal = Animal()
# animal.sound()
# animal.grow()
# animal.run()
# plant = Plant()
# plant.grow()
# plant.photosynthesize()



# 3) Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.
# Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:


# from abc import ABC, abstractmethod
# class Planet(ABC):
#     def __init__(self, orbit):
#        self.orbit = orbit

#     @abstractmethod       
#     def get_age(self):
#         ...
        
      
# class Mercury(Planet):
#     def __init__(self, orbit):
#        super().__init__(orbit)
       
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет'

# class Venus(Planet):
#     def __init__(self, orbit):
#        super().__init__(orbit)
    
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round((earth_age / (self.orbit / 365))*365)} дней'
    
# class Jupiter(Planet):
#     def __init__(self, orbit):
#        super().__init__(orbit)

#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'
   
# mercury = Mercury(88)
# venus = Venus(225)
# jupiter = Jupiter(12)

# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))










# 1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name) 
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def __validate_name(self, name):
#         if len(name) < 2:
#             name = "John"
#             return name
#         else:
#             return name.capitalize()
#     @property
#     def number(self):
#         return self._phone_number

#     @property
#     def card_number(self):
#         return self.__card_number
    

    
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam.name)
# print(sam.number)
# print(sam.card_number)



# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_ = {k: v for k,v in dict_.items() if v is None}
# print(dict_)



# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {k ** 2: v for k,v in dict1.items()}
# print(dict2)


# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {k: len(k) for k in list_}
# print(dict_)

# dict_ = {'Makers': 6, 'coding': 6, 'hello': 5}
# dictmax = max(dict_.values())
# for k,v in dict_.items():
#     if v == dictmax:
#         print(k)


# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {k: v ** 3  for k,v in dict1.items()}
# print(dict2)


# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict_ = {k: v_inner for k,v_outer in dict_.items() for v_inner in v_outer.values()}
# print(dict_)



# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# dict1 = dict_.copy()
# for k, v in dict1.items(): 
#     for value in v.values(): 
#         dict_[k]=value 
                
# print(dict_)

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k, v in dict1.items():
#     a = 1
#     for value in v.values(): 
#         a = a * value
#         dict2[k] = a 
# print(dict2)

# import math
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {k: math.prod(v.values()) for k,v in dict1.items()}
# print(dict2)



# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# list_str = [x for x in list_ if isinstance(x, str)]
# list_int = [x for x in list_ if isinstance(x, int)]
# dict_ = dict(zip(list_str, list_int))
# print(dict_)




# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_dict = {k:item for item in sorted(dict_.values()) for k,v in dict_.items() if item == v} 
# print(sorted_dict)


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# for item in sorted(dict_.values()):
#     for k,v in dict_.items():
#         if item == v:
#             sorted_dict[k] = item

# print(sorted_dict)


# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=lambda x: x[1]))
# print(sorted_dict)

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=lambda x: x[1], reverse= True))
# print(sorted_dict)

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# list_ = [k for k in dict_ if k == int(key)]

# if len(list_) > 0:
#     print('Key is present in the dictionary')
# else:
#     print('Key is not present in the dictionary')



    

import openai
import os
import json
from base64 import b16decode

piompt = input('The piompt: ')
openai.api_key = os.getenv('API_KEY')















