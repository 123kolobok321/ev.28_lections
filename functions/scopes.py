## область видимости и пространства имён (scopes)
# это технология которая определяет контекст иени (переменные) в рамках которого мы можем её использовать

# built-ins(Встроенная область видимости)-> print,len,max
# global(Глобальная)-> область одного файла
# enclosed(не локальная(замкнутая), nonlocal)
# local(локальная)-> область внутри одной функции


# x = 200
# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a 
# myFunc()
# # print(a)
# print(x)

# a = 10 # global
# print # built-in
# def hello(): # global
#     a = 'Hello world' # local
#     print(a, 'local inside in func!')

# hello()
# print(a, 'global')

### LEGB - local enclosed global built-in

###################################
#Enclosed
# замкнутое пространство имён - локальное пространство, у которого усть внутренее 
# (вложенное пространство) локальное пространство

# x = 'global'
# print(x) # global

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x) # local
#     print(x)
#     local()
#     print(x)

# enclosed()
# print(x)

# a = 5

# def func():
#     print(a)
#     a = a + 1
# func()

# nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри локальной области

# var = 100

# def increment(): # LEGB
#     global var
#     var += 1 # var = var + 1

# print(var)
# increment()
# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)


# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1 
#         return num
#     return increment


# print(globals())
# c = counter()
# # print(c) #<function counter.<locals>.increment at 0x7fcc0d5d2050>
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# print(c())
# # print(counter())

# def func():
#     return 'John Snow'

# a = func
# print(a)


# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# globals - func которая возвращает все имена внутри глобальной области видимости

# locals - функция которая возвращает все имена внутри глобальной области видимости и локальной

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1 
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
#     print()

# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0

# print('Приветсвую вас, король севера John Snow, в Вестеросе!')
# while True:
#     print('Тебе доступны слейдующие действия:')
#     print('1-убить героя, 2-убить моба, 3-статистика 4-выйти из игры')
#     choice = input('Ввидите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = counter_heroes()
#         print()
#         print('Вы обеглавили Ланистера!')
#     elif choice == '2':
#         mobs = counter_mobs()
#         print()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes, mobs)
    
#     elif choice == '4':
#         print('Пока пока! Ждём еще раз!')
#         break
    









































