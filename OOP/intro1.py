#  ООП - обьектно ориентированное программирование

#  Класс -> это описание того, как должен выглядеть обьект, то есть в классе мы описываем какими свойствами (данными) и поведением(функции) должен обладать обьект

# Обьект -> это сущьность которую мы создаём от класса, у обьекта есть собственное состояние свойств(данные)

# Целью создания было связать данные с функциями которые управляли этими данными

# Свойствами(атрибутами)- называют обычные переменные внутри класса в которых храняться данные обьекта

# Методы - это обычные функции внутри класса, методы описывают поведение обьекта


###################################################################################

# class Human:
#     age = 0

#     def __init__(self, first_name, Last_name, job, citizenship):
#          self.name = first_name + ' '+ Last_name
#          self.job = job
#          self.citizen = citizenship

#     def snow_info(self):
#          return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'
    
# john = Human('John', 'Snow', 'King of North', 'Northerner')
# bilal = Human('Bilal', 'Lanister', 'Programmist', 'KR')

# # print(john, type(john))
# # print(dir(john))
# print(john.snow_info())
# john.age = 24
# print(john.snow_info())
# john.job = 'King of Westeros'
# print(john.snow_info())
# print()
# print(bilal.snow_info())


####################################################################

# class Dog:
#     # атрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name: str, color: str)-> None:
#         """Инициализатор, именно здесь создаются атрибуты обьекта"""
#         # self - ссылка на обьект который только что создался
#         self.name = name 
#         self.color = color

#     def bark(self):
#         print(f'{self.name} лает!')

#     def snow_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')

# rex = Dog('Rex', 'black')
# pluto = Dog(name='Pluto', color='brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.snow_info()
# pluto.snow_info()
# aktosh.snow_info()

# rex.age = 2
# pluto.age = 5
# aktosh.age = 3
# aktosh.ushi = False

# rex.snow_info()
# pluto.snow_info()
# aktosh.snow_info()


# rex.bark()
# pluto.bark()


#########################################################################

# class Human:
#     def __init__(self):
#         print('init worked!')
#         self.raychel = 'raychel'
#         self.golod = 100

#     def eat(self, meal, doela=True):
#         print(f"{self.raychel} покушала {meal}")
#         if doela:
#             self.golod -= 50
#         else:
#             self.golod -= 25    
        

# obj = Human()
# print(obj.raychel, obj.golod)
# obj.eat('burger', doela=False)
# print(obj.raychel, obj.golod)
# obj.eat('Kruasan')
# print(obj.raychel, obj.golod)









