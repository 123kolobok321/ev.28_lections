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


# import json 
# def bulk_create(products): 
#     with open('db.json') as f: old = json.load(f) 
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






from bs4 import BeautifulSoup
import requests
import lxml
source = requests.get('https://enter.kg/').text
my_page = BeautifulSoup(source,'lxml')











































