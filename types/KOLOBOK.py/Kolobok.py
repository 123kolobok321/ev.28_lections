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















































































































