# dict()- Словарь -> упорядочная коллекция элементов(python 3.7 -> ordered). 
# Каждый элемент внутри словаря хранится в виде пары --> {ключь: значение}

# ассоциативный масив, hash table, object(js), strukture == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре только уникальные ключи
# тогда как значениями могут выступать любые типы данных.


# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }

# print(thisdict)
# print(type(thisdict))
# print(thisdict['brand'],thisdict['model'])
# print(thisdict['year'])

# thisdict['motor'] = 'GTE Turbo'
# thisdict['brand'] = 'Tesla'
# print(thisdict)


# a = {}
# a = {1,2,3,4,}
# a = set()
# print(a)
# print(type(a))

# a = {}
# b = dict()

#-----------------------------------------------------
#print(dir(dict))
# items , keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }
# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])


# ls = list(user_info.values())
# print(ls)

# items = user_info.items()
# print(items)
# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# for x in user_info.items():
#     print(f'keys: {x[0]}, value: {x[1]}')
#     for key, value in user_info.items():
#         print(f'keys: {key}, values: {value}')
#     print(x)

# изменение значения в словаре

# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['age'] = 24
# dict_['address'] = 'WinterFell'
# print(dict_)
# dict_.update({'age': 25, 'address': 'BlackCastle'})
# print(dict_)


#-_______________________________________

#  получение данных со словоря
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(8))


#setdefault - работает так же как get, но если нет такого ключа то создаёт новую пару из этого ключа 

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, 'Manty'))
# print(dict_)

# _________________________________

# создание -fromkeys 
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, 'Kolobok')
# print(new_dict)

# -----------------------------
# удоление элементов
# pop, popitem

# pop(<key>) - удоляет пару по ключу
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)


# popitem - удоляет последнию пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)




#----------------------------------------------------
# roles = {
#     0: 'Admin',
#     1: 'Customer',
#     2: 'Vendor',
# }

# users = {
#     1:{
#     'id': 1, 'role': roles[2], 'username': 'Triton'
#     },
#     2:{
#     'id': 2, 'role': roles[0], 'username': 'John Snow'
#     },
#     3:{
#     'id': 3, 'role': roles[1], 'username': 'Raychel'
#     },
# }
# print(users)


# product = {
#     'id': 1,
#     'title': 'Samsung Galaxy A51',
#     'description': 'Lorem Ipsum',
#     'price': 250,
# }
# print(product)

# id_user = int(input('Vvedite id:'))
# if users[id_user]['role'] == roles [0]:
#     product['description'] = input('Vvedite opisanie:')
# else:
#     print('You do not have permissions!')

# print(product)

#





# a = {'a': 1, 'b': 2, 'c': 1}
# remuved = a.pop('c')
# print(remuved)

# a = {'a': 1, 'b': 2, 'c': 1}
# print(a)
# b = a.fromkeys({'ls': 5})
# print(b)




# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)



# a = {'a': 1, 'b': 2, 'c': 1}
# a.dict. clear({'a': 1, 'b': 2, 'c': 1})
# print(a)

# a = {'a': 1, 'b': 2, 'c': 1}
# dict.clear({'a': 1, 'b': 2, 'c': 1})
# print()

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)


# task 5
# a = {'a': 1, 'b': 2, 'c': 1} 

# print(b)in a.items(): 
#     b.append(k) 
# print(b)

# task6
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# task7
# a = {'a': 1, 'b': 2, 'c': 1}
# for k in a:
#     print(k)


# task 8
# a = {'a': 1, 'b': 2, 'c': 1}
# for x, z in a.items(): 
#     print(z) 

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2==0: b.setdefault(k, 2) 
# else: b.setdefault(k,v) 
# print(b)


# task 9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for k, v in a.items(): 
#     if v%2 == 0: 
#         b.setdefault(k, 2) 
#     else: 
#         b.setdefault(k,v) 
# print(b)






# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(a.items()):
#     if v == None:
#         a.pop(k)
    
# print(a)
# # 
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# # print(a)
# removed = a.pop('a')
# removed2 = a.pop('d')
# print(a)
# # print(removed2)
# # print(removed)




















































































