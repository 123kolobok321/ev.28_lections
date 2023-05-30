"""
Абстракция
"""
# Абстракция (Абстрактный класс) - принцып ООП, в котором создаётся абстрактный класс (класс - пустышка), в котором создаются названия атрибутов и методов, для того чтобы в дочерних классах переопределить их нужным образом. (у нас есть название, но нет логики)

# from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

# class AbstractAnimal(ABC):

#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
        # ...

# # @abstractmethod - декоратор который требует переопределение метода в наследуемом классе

# # @abstractproperty - декоратор который требует переопределения атрибутов класса

# # obj = AbstractAnimal()  TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice      

# class Dog(AbstractAnimal):
#     ...

# obj = Dog() # Error

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('гав-гав')

# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('meow')

# dog  = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)
# dog.voice()
# print(dog.legs)


# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2
    
# obj = Square(25)
# obj.name
# print(obj.area())








































