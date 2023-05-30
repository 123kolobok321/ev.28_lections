# magic methods(магические методы)
# Dunder methods (double underscore)-> __init__
# Служебные методы

# Магия (фишка ) заключается в том что эти методы запускаются без прямого обращения к ним, определённые методы могут отвечать за определённые операторы

# class A(int):
#     pass

# obj = A()
# print(dir(obj))

# Магические методы сравнения

# __eq__(self, other) -> 5 == 8


# __ne__ -> !=

# __lt__ -> <

# __gt__ -> >

# __le__ -> <=


# __ge__ -> >=


# print('15' < 'ABC')
# print(ord('1'), ord('A'))

# class Word(str):
#     def __new__(cls, obj):
#         # print(cls, '!!!')
#         # print(obj, '!!!')
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __gt__(self, other) -> bool:
#         print('gt сработал')
#         print(self)
#         print(other)    
#         return len(self) > len(other)
    
#     def __lt__(self, _value) -> bool:
#         return len(self) < len(_value)
    
#     def __eq__(self, _value) -> bool:
#         return len(self) == len(_value)

# obj = Word('   word defo ')
# obj1 = Word('  V akw        err')

# print(obj > obj1)
# print(obj1 < obj)
# print(obj == obj1)

###################################################

# + - / * // % **

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __truediv__ (py2) __div__
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
#         # if not 0 < number < 100:
#         #     raise ValueError('Enter the number in range 0-100')
#         # return cls(number)
    
    
#     def __add__(self, other):
#         print('add вызвана')
#         res = self.number + other.number
#         print(f'Result: {self.number} + {other.number} = {res}') # % * ** / //


# value1 = Cifra(-177)
# value2 = Cifra(66)
# value1 + value2

##################################################################
# from random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')

# class Cat:
#     def sound(self):
#         print('Meow meow!')

# class Lion:
#     def sound(self):
#         print('Roar!')

# class Pet:
#     def __new__(cls):
#         other = choice([Dog, Cat, Lion])
#         instance = super().__new__(other)
#         print(f'I\'m {type(instance).__name__}')
#         return instance
    
#     def __init__(self) -> None:
#         print('Pet never was called!')


# pet = Pet()
# pet.sound()

#################################################################
# SINGLETON

# class SingLeton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __str__(self) -> str:
#         return str(id(self))


# a = SingLeton()
# b = SingLeton()
# print(a)
# print(b)
# print(a is b)


################################################################
# дандер методы строкового отображения обьектов
# __str__
# __repr__

# class Base:
#     def __init__(self, stroka):
#         self.string = stroka

#     def __str__(self) -> str:
#         return f'Обьект: {self.string}'
    
#     def __repr__(self) -> str:
#         return "Base('Example')"
    
# obj = Base('Vasya')
# print(obj)
# print(repr(obj))
# obj2 = Base('Kolobok')
# print(obj2)
# obj3 = eval(repr(obj2))
# print(obj3)
# # eval

################################################

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index - 1]

# obj = Kopilka()
# obj.add_coin(99)
# obj.add_coin(9)
# obj.add_coin(9999)
# print(obj.coins)
# print(obj.total)
# print(len(obj))
# print(obj[1])

# for x in obj:
#     print(x)






















class A:
    def hello(self):
        print('hello world')

class B:
    def hello(self):
        print('HELLO WORLD')

class C(A, B):
    pass
obj = C()
obj.hello()


























































































