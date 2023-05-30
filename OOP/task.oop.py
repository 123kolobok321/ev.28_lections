# class Song:
#     def __init__(self,author,title,year):
#         self.author = author
#         self.title = title
#         self.year = year

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'
    
    
# song = Song("Happy", 'Pharrell Williams', 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())



# class Circle:
#     color = 'Blue'
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.pi*(self.radius**2)
# circle = Circle(radius = 13)        
# circle.color = 'Red'
# circle.get_area() 


# class Circle: 
#     color='Синий' 
#     pi = 3.14 
#     def __init__(self,radius=int): 
#         self.radius = radius 
#     def get_area(self): 
#         result = self.pi * self.radius**2 
#         return result 
    
# circle = Circle(2) 
# circle.color = 'Чёрный'
# print(circle.color) 
# print(circle.get_area())



# class Polygon:
#     width = 0
#     height = 0
#     def set_values( self, width, height):
#         Polygon.width = width
#         Polygon.height = height

# class Rectangle(Polygon):
#     def area(self):
#         return self.width * self.height

# class Triangle(Polygon):
#     def area(self):
#         return(self.width * self.height) / 2

# rect = Rectangle()
# trey = Triangle()

# rect.set_values(4, 5)
# trey.set_values(4, 5)

# print('Rectangle Area:', rect.area())
# print('Triangle Area:', trey.area())


# class BankAccount: 
    
#     def __init__(self): 
#         self.balance = 0 
#     def withdraw(self, amount): 
#         self.balance -= amount 
#         print(f'Ваш баланс: {self.balance} сом') 
#     def deposit(self, amount): 
#         self.balance += amount 
#         print(f'Ваш баланс: {self.balance} сом') 
# account = BankAccount() 
# account.deposit(1000) 
# account.withdraw(500)


# class Taxi: 
#     def __init__(self, name, cost, cost_km): 
#         self.name = name 
#         self.cost = cost 
#         self.cost_km = cost_km 


#     def get_total_cost(self, km): 
#         self.cost = self.cost_km * km + self.cost 
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом'
     
# taxi1 = Taxi(name='Namba',cost=29, cost_km=27) 
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=198) 
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=10) 

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))




# class Phone:

#     def init(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()


# class Phone: 
#     def __init__(self, name, last_name, phone) -> None: 
#         self.name = name 
#         self.last_name = last_name 
#         self.phone = phone 
        
#     def get_info(self): 
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', '+996707707707') 
# contact.get_info()



# class Salary: 
#     percent = 8 
#     def __init__(self, salary, experience): 
#         self.salary = salary 
#         self.experience = experience 
    
#     def count_percent(self): 
#         return self.salary * self.percent / 100 * self.experience 

# obj = Salary(10000, 8) 
# print(obj.count_percent())







# class Nobel(): 
#     from datetime import datetime
#     a = datetime.now()

#     def __init__(self, category, year, winner) -> None: 
#         self.category = category 
#         self.year = year 
#         self.winner = winner 
        
#     def get_year(self): 
#         res = self.a.year - self.year 
#         return f'выиграл {res} лет назад' 

# winner1 = Nobel('Литература', 1971, 'Пабло Неруда')
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())


# class T1:
#     def __init__(self):
#         self.n = 10
#     def total(self, a):
#         return self.n + int(a)
# class T2:
#     def __init__(self):
#         self.string = 'Hi'
#     def total(self, a):
#         return len(self.string + str(a))
# t1 = T1()
# t2 = T2()
# print(t1.total(35))  # Вывод: 45
# print(t2.total(35))  # Вывод: 4



# class Rectangle:
#     def __init__(self, width, height, sign):
#         self.w = int(width)
#         self.h = int(height)
#         self.s = str(sign)
#     def __str__(self):
#         rect = []
#         # количество строк
#         for i in range(self.h):
#             # знак повторяется w раз
#             rect.append(self.s * self.w)
#         # превращаем список в строку
#         rect = '\n'.join(rect)
#         return rect
# b = Rectangle(10, 3, '*')
# print(b)  


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):

#         print("Bark")

# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()


# class Polygon:
#     width = 0
#     height = 0
#     def set_values( self, width, height):
#         Polygon.width = width
#         Polygon.height = height

# class Rectangle(Polygon):
#     def area(self):
#         return self.width * self.height

# class Triangle(Polygon):
#     def area(self):
#         return(self.width * self.height) / 2

# rect = Rectangle()
# trey = Triangle()

# rect.set_values(4, 5)
# trey.set_values(4, 5)

# print('Rectangle Area:', rect.area())
# print('Triangle Area:', trey.area())


# class Mydict(dict):
#     def get(self, key, default = 0):
#         return dict.get(self, key, default)

# a = dict(a=1, b=2)
# b = Mydict(a=1, b=2)



# class Person(object):
#     # Constructor
#    def __init__(self, name):
#        self.name = name

#     # To get name
#    def get_name(self):
#        return self.name

#     # To check if this person is Student
#    def is_student(self):
#        return True

# person = Person("Влад")  # An Object of Person
# print(person.get_name(), person.is_student())


# class ElectricCar: 
#      def use_batteries(self): 
#          print('использую электричество') 

# class RegularCar: 
#      def use_gasoline(self): 
#          print('использую бензин') 

# class Hybrid(ElectricCar, RegularCar): 
#      pass 

# car = Hybrid() 
# car.use_batteries() 
# car.use_gasoline() 


# class Auto:
#      def ride(self):
#           print('Riding on a ground')

# class Boat:
#      def swim(self):
#           print('Floating on water')


# class Amphibian(Auto,Boat):
#      def obj(self):
#         pass  

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 



# class Borsh: 
#      pass

# class Salad: 
#      pass 

# class SaltMixin: 
#      def salt(self): 
#          print('посолили') 

# class PepperMixin: 
#      def pepper(self): 
#          print('поперчили')
 
# class Borsh(SaltMixin, PepperMixin): 
#      pass  
# class Salad(SaltMixin): 
#      pass 

# sup = Borsh() 
# sup.salt() 
# sup.pepper() 


# class RadioMixin:
#     def play_music(self, title):
#         self.play_music = title
          
# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# print(obj.play_music('Rock'))
# print(auto.play_music('Classic'))       
# print(boat.play_music('Pop'))



# class A: 
#      def method(self): 
#          print('метод класса А')

# class B: 
#      def method(self): 
#          print('метод класса B')

# class C(A,B): 
#      pass 

# c = C() 
# c.method() 

# class A: 
#      pass

# class B: 
#      def method(self): 
#          print('метод класса B') 

# class C(A,B): 
#      pass 

# c = C() 
# c.method() 



# class Clock:
#     from datetime import datetime 
#     time_now = datetime.today().strftime("%H:%M:%S")
#     def current_time(self):
#         print(self.time_now)

# class Alarm:
#     def on(self):
#         print('Будильник включен')
          
#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         self.on()

# clock = AlarmClock()
# clock.current_time() 
# clock.alarm_on()  

# from abc import ABC, abstractmethod
# class Coder(ABC):
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         pass
#     def coding(self):
#         pass

# class Backend(Coder, experience, languages_backend):
    
    

# class Frontend(Coder):
   






# from abc import ABC, abstractmethod 
# class Coder(ABC): 
#     count_code_time = 0 

# @abstractmethod 
# def get_info(self): 
#     pass 

# @abstractmethod 
# def coding(self, hours): 
#     pass 

# class Backend(Coder): 
#     def __init__(self, experience, languages_backend): 
#         self.experience = experience 
#         self.languages_backend = languages_backend 
#     def get_info(self): 
#         return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): self.count_code_time += hours 

# class Frontend(Coder): 
#     def __init__(self, experience, languages_frontend): 
#         self.experience = experience 
#         self.languages_frontend = languages_frontend 
#     def get_info(self): 
#         return f"{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование" 
#     def coding(self, hours): self.count_code_time += hours 

# class Fullstack(Backend, Frontend): 
#                 pass 
# a = Backend('Junior', 'Python') 
# b = Frontend('Middle', 'JavaScript') 
# c = Fullstack('Senior', 'Python and JS') 
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info())



# class A:
#     def public(self):
#         return 'Public method'
    
#     def _protected(self):
#         return 'Protected method'
    
#     def __private(self):
#         return 'Private method'
    

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())


# class A:
#     def method1(self):
#         print("Hello World")

# class B(A):
#     pass

# b1 = B()
# b1.method1()


# class Phone:

#     def __init__(self, passcode): 
#         self.__passcode = passcode

#     def get_passcode(self): 
#         return self.__passcode
    
#     def set_passcode(self, new): 
#         self.__passcode = new 


# myphone = Phone(1234) 
# myphone.set_passcode(9876) 
# print(myphone.get_passcode()) 



# class Car: 
#     __speed = 0 
#     def set_speed(self,new): 
#         self.__speed = new 
#         return self.__speed 
#     def show_speed(self): 
#         return self.__speed 
    
# car1=Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed())


# class Phone: 
#   def __init__(self, passcode): 
#       self.__passcode = passcode 
 
#   @property 
#   def code(self): 
#       return self.__passcode

#   @code.setter 
#   def code(self, new): 
#       self.__passcode = new  


# myphone = Phone(1234) 
# print(myphone.code) 
# myphone.code = 4321 
# print(myphone.code)


# class Car: 
#     __speed=0 
#     @property 
#     def speed(self): 
#         return self.__speed 
#     @speed.setter 
#     def speed(self,new): 
#         self.__speed=new 
#         return self.__speed 
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)


# class Post:
#     id = 0

#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []

#     # CRUD
#     def create_post(self, title, body, image):
#         Post.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'successfully created'}
    
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return {'status': 200, 'content': post}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post['id'] == post_id:
#                 index = self.posts.index(post)
#                 self.posts[index].update(**kwargs)
#                 return {'status': 200, 'msg': 'updated'}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.remove(post)
#                 return {'status': 204, 'msg': 'No content!'}
#         return {'status': 404, 'msg': 'Not found!'}

# acc1 = Post('JohnSnow')
# acc2 = Post('JamieLanister')

# acc1.create_post('Good News', 'Sansa rodila dochku!!', 'http://localhost:8000/images/foto.jpg')
# acc1.create_post('Na progulke!', 'na chile', 'http://foto.jpg')
# acc1.create_post('Egipet!!', 'Lechu v Egipet', 'http://goto123.jpg')

# acc2.create_post('Jamie', 'Post Jamie', 'https://jamie.jpg')

# acc1.create_post('Turkey!!', 'Lechu v Turkey', 'http://goto123.jpg')

# print(acc1.user)
# print(acc1.posts)
# print(acc2.posts)

# print(acc1.retrieve_post(1))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(1, title='Suyunchu!!'))

# print(acc1.retrieve_post(1))
# print(acc1.delete_post(1))

# print(acc1.posts)
# print(acc2.posts)


# Анатация свойств(@property(getter, setter))

# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '996'
#     __number = '555666777'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         print(self.__name)
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             print('Invalid value for name!')
#         else:
#             print('Setter', value)
#             self.__name = value

# obj = Person()
# obj.name
# obj.name = 'Jamie'
# obj.name

# Анатация свойств(@property(getter, setter))

# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '996'
#     __number = '555666777'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         print(self.__name)
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             print('Invalid value for name!')
#         else:
#             print('Setter', value)
#             self.__name = value

#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0, 150):
#             print('Invalid Values')
#         else:
#             self.__age = value 
#     @property
#     def number(self):
#         name = input('Vvedite svoye imya: ')
#         if self.__name == name:
#             print('Invalid name!')
#         else:
#             print(self.__full_number)

# obj = Person()
# obj.name
# obj.name = 'Jamie'
# obj.name
# obj.age
# obj.age = 30
# obj.age
# obj.number



# class T1:
#     def __init__(self):
#         self.n = 10
#     def total(self, a):
#         return self.n + int(a)
# class T2:
#     def __init__(self):
#         self.string = 'Hi'
#     def total(self, a):
#         return len(self.string + str(a))
# t1 = T1()
# t2 = T2()
# print(t1.total(35))  # Вывод: 45
# print(t2.total(35))  # Вывод: 4

# class MyClass: 
#      def __init__(self, name): 
#          self.name = name 

#      def __str__(self): 
#          return self.name

# obj = MyClass('первый объект') 
# print(obj) 

# class Password:
#     def __init__(self, str_) -> None:
#         self.str_ = str_
    
#     def validate(self):
#         if self.str_ == 8 and self.str_ < 15:
#             raise ValueError('Password should be longer than 8, and less than 15')
#         elif not any(map(lambda x: x.isdigit()), self.str_):
#             raise ValueError('Password should contain numbers too')
#         elif not any(map(lambda x: x.isalpha()), self.str_):
#             raise ValueError('Password should contain letters as well')
#         elif not any(map(lambda x: x in ['@', '#', '&', '$', '%', '!', '~', '*'], self.str_)):
#             raise ValueError('Your password should have some symbols')
#         else:
#             return 'Ваш пароль сохранен.'
        
  
#     def __str__(self) -> str:
#         return '*' * len(self.str_)
        
    
# pas = Password('joe@123456')
# print(pas.validate())
# print(pas)
    

     
        
# class Password:

#     def __init__(self, password): 
#         self.password = password

#     def __str__(self) -> str:
#         return '*' * len(self.password)

#     def validate(self):
#         if len(self.password) == 8 and len(self.password) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         elif not any(map(lambda x: x.isdigit()), self.password):
#             return f'Password should contain numbers too'
#         elif not any(map(lambda x: x.isalpha()), self.password):
#             return f'Password should contain letters as well'
#         elif not any(map(lambda x: x in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)):
#             return f'Your password should have some symbols'
#         return f'Ваш пароль сохранен.'     

 
        
# passw = Password('Ert2e@wew')
# print(passw.validate())
# print(passw)
        


# class Password:

#     def __init__(self, password) -> None:
#         self.passw = password

#     def validate(self):
#         if len(self.passw) == 8 and len(self.passw) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         elif not any(list(map(lambda x: x.isdigit(), self.passw))):
#             return f'Password should contain numbers too'
#         elif not any(list(map(lambda x: x.isalpha(), self.passw))):
#             return f'Password should contain letters as well'
#         elif not any(list(map(lambda x: x in ['@', '#', '&', '$', '%', '!', '~', '*'], self.passw))):
#             return f'Your password should have some symbols'
#         else:
#             return f'Ваш пароль сохранен.'

#     def __str__(self) -> str:
#         return "*" * len(self.passw)
    
# password = Password('joe@123456')
# print(password.validate())
# print(password)


# class Math:

#     def __init__(self, number) -> None:
#         self.number = number

#     def get_factorial(self):
#         from math import factorial
#         return factorial(self.number)
    
#     def get_sum(self):
#         a = sum([int(x) for x in str(self.number)])
#         return a 
        
#     def get_mul_table(self):
#         res = ''
#         for x in range(1, 11):
#             res = res + f'{self.number} x {x} = {self.number * x}\n'

#         return res

# math1 = Math(11) 
# print(math1.get_factorial()) 
# print(math1.get_sum())
# print(math1.get_mul_table())  
       
        


#

     



# class Dog:
#     def sound(self):
#         print('Гав')

# class Cat:
#     def sound(self):
#         print('Мяу')


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







# class Cat:
#     def __init__(self, name):
#         self.name = name
        

#     def info(self):
#         print(f"I am a cat. My name is {self.name}")

#     def voice(self):
#         print("Мяу")

# class Dog:
#     def __init__(self, name):
#         self.name = name
        

#     def info(self):
#         print(f"I am a dog. My name is {self.name}")

#     def voice(self):

#         print("Гав")

# cat1 = Cat("barsik")
# dog1 = Dog("rex")
# cat1.voice()
# dog1.voice()







# 3) Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.
# Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

# !!!!!
# обязательное условие: создание абстрактного метода
# !!!!!

# from abc import ABC, abstractmethod
# from datetime import datetime
#.strptime()
# class Planet:
#     def __init__(self, orbit, get_age, earth_age):
#         self.orbit = orbit
#         self.get_age = get_age
#         self.earth_age = earth_age

# @abstractmethod
# class Mercury(Planet):
#     def __init__(self, orbit, get_age, earth_age):
#         super().__init__(orbit, get_age, earth_age)
#         return f'состовляет {self.orbit} земных дней'

# @abstractmethod
# class Venus(Planet):
#     def __init__(self, orbit, get_age, earth_age):
#         super().__init__(orbit, get_age, earth_age)
#         return f'состовляет {self.orbit} земных дней'
    
# @abstractmethod    
# class Jupiter(Planet):
#     def __init__(self, orbit, get_age, earth_age):
#         super().__init__(orbit, get_age, earth_age)
#         return f'состовляет {self.orbit} земных дней'

   
# mercury = Mercury(Planet)
# venus = Venus(Planet)
# jupiter = Jupiter(Planet)
# mercury.orbit(88)
# venus.orbit(225)
# jupiter.orbit(12)










# 2) Создайте 3 класса:
# Bird, Animal, Plant
# класс Bird должен иметь методы: fly(), grow(), sound(). Animal: sound(), run(), grow(). Plant: grow(), photosynthesize()
# каждый метод должен просто принтить действие. Например: def fly(self): print('я лечу')

# !!!!
# Обязательное условие: использовать абстракцию. Если не переопределить общий метод должна выходить ошибка
# !!!!!






# 1)Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов. С помощью list comprehension создайте список из результатов работы метода count обоих объектов.

# !!!! 
# Обязательное условие: если в классе A или B не переопределить метод count должна выйти ошибка
# !!!!


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





# class CustomNumber:

#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
       
#     def __sub__(self, other):
#         res = self.number + other.number
#         return res
    
#     def __add__(self, other):
#         res = self.number - other.number
#         return res
    
#     def __mul__(self, other):
#         res = self.number / other.number
#         return res
    
#     def __truediv__(self, other):
#         res = self.number * other.number
#         return res
    
#     def __eq__(self, other):
#         return self.number != other.number
    
#     def __ne__(self, other):
#         return self.number == other.number
    
#     def __lt__(self, other):
#         return self.number > other.number
    
#     def __gt__(self, other):
#         return self.number < other.number
    
#     def __le__(self, other):
#         return self.number <= other.number
    
#     def __ge__(self, other):
#         return self.number >= other.number
         

    


# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 5
# print(num2 - num1)  # 15
# print(num1 * num2)  # 2.0
# print(num2 / num1)  # 0.5

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 < num2)   # False
# print(num1 > num2)   # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True








# class ToDo: 
#     def __init__(self,string): 
#         self.todo = string 
#         self.instances = dict()

#     def give_priority(self,priority): 
#         ToDo.instances[priority] = self.todo 

#     def list_of_tasks(self,): 
#         return sorted(ToDo.instances.items())
    
# priority = ToDo()
# priority.list_of_tasks()
   
# priority = ToDo()
# priority.list_of_tasks()
   
# priority = ToDo()
# priority.list_of_tasks()



# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(min(dict_.values()))

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}


# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {k:v if v % 2 == 0 else 1 for (k,v) in dict1.items()} 
# print(dict2)



# class BaseEstimator:
#     def __init__(self, name, **kwargs):
#         self.name = name
#         super().__init__(**kwargs)

#     def __repr__(self):
#         return f', '.join(f'{k}: {v}' for k, v in vars(self).items())

# class ServingMixin:
#     def __init__(self, mode, **kwargs):
#         super().__init__(**kwargs)
#         self.mode = mode

# class DecisionTree(BaseEstimator, ServingMixin):
#     def __init__(self, depth, **kwargs):
#         super().__init__(**kwargs)
#         self.depth = depth

# dt = DecisionTree(name='Request Time DT', depth=1, mode='online')
# print(dt)
# print(dt.mode)


# def divide(a, b):
#     return a / b
    
# print(divide(5, 10)) 


# def get_elems(my_list):
#       for element in my_list:
#           print(element)   

# get_elems(['first', 'second', 'third'])


# dict_={1:'a', 2:'b', 3: 'c', 4:'d'} 
# def dictionary(dict_): 
#     for k in dict_: 
#         print(k) 
        
# dictionary(dict_)


# def check_type(elem): 
#     if type(elem) == str: 
#         print('это строка') 
#     elif type(elem) == int: 
#         print('это число') 
#     else: 
#         print('что-то другое') 

# check_type(10) 

# num = 6
# def check(num):
#     if num % 2 != 0:
#         return ("It is odd number")
#     else: 
#         return ("It is even number")

# print(check(num)) 


# # num = 6 
# # def check(num): 
# #     if num % 2 == 0: 
# #         return("It is even number") 
# #     else: 
# #         return("It is odd number")




# 1) Создайте класс MyString, который будет наследоваться от str.
# Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример:
# example = MyString('String')
# example.append('hello')
# print(example) -> 'Stringhello'
# print(example.pop()) -> 'o'
# print(example) -> 'Stringhell'


# class MyString(str):
#     def append(self, str_):
#         self.str_ = str_

        
#     def pop(self, pop_):
#         self.pop_ = pop_   


# example = MyString('String')
# example.append('hello')
# print(example, 'Stringhello') 
# print(example.pop('o'))  
# print(example, 'Stringhell') 


# 2)Dollar.
# Создайте функцию dollarize, которая принимает дробное число (float) и переводит его в
# долларизованный формат:
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
# Создайте класс MoneyFmt, который содержит один единственный атрибут amount и 4 метода:
# init - инициализирует значение атрибута amount
# update - задаёт объекту новое значение amount
# repr - возвращает значение float
# str - метод, который реализует логику функции dollarize()
# //Вывод должен выглядеть следующим образом:
# cash = MoneyFmt(12345678.021)
# print(cash) -- выводит "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- выводит "$100,000.46"
# cash.update(-0.3)
# print(cash) -- выводит "-$0.30"
# repr(cash) -- выводит -0.3

# class MoneyFmt:
#     def dollarize(self, amount):
#         self.amount = amount

#     def __init__(self, amount):
#         self.amount = amount

#     def update(self,amount):
#         self.amount = amount

#     def __repr__(self, amount) -> str:
#         self.amount = amount
        
#     def __str__(self, amount) -> str:
#         self.amount = amount
        


# cash = MoneyFmt(12345678.021)
# print(cash.amount) 
# cash.update(100000.4567)
# print(cash.amount) 
# cash.update(-0.3)
# print(cash.amount) 
# repr(cash.amount) 


# 3) Велосипед.
# Создайте класс Bike в котором будут инициализированы следующие атрибуты: self.cost
# (стоимость)
# self.make (производитель)
# self.model (модель)
# self.year (год выпуска)
# self.condition (состояние)
# self._sale_price = None (цена для продажи, по умолчанию None)
# self.sold = False (продан или нет, по умолчания False)
# Также укажите мин. прибыль, которая должна прийти с продажи велосипеда. Создайте метод
# для указания цены для продажи, который принимает цену и если она меньше стоимости, то
# ставит дефолтную цену для продажи (стоимость + мин. прибыль).
# Для ремонта велосипеда будет использоваться метод service, которая принимает стоимость
# ремонта и новое состояние велосипеда, соответственно продажная цена велосипеда
# возрастает на столько, сколько обошелся ремонт и возвращает нынешнюю цену для продажи.
# При продаже велосипеда будет использоваться метод sell, который меняет значение self.sold на

# True и возвращает прибыль с продажи.
# Допишите метод get_default_bike, который будет создавать дефолтный велосипед. Создайте
# объект bike = Bike.get_default_bike() и используете его методы и получите значения всех его
# атрибутов.
# """


# class Bike:
#     def __init__(self, cost, make, model, year, condition, _sale_price, sold) -> None:
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self._sale_price = None
#         self.sold = False

#     def get_default_bike(self):

    

#     def service(self, _sale_price):


# bike = Bike.get_default_bike()



# class ToDo: 
#     def __init__(self,string): 
#         self.todo=string 
#         ToDo.instances=dict() 
    
#     def give_priority(self,priority): 
#         ToDo.instances[priority]=self.todo 
    
#     def list_of_tasks(self): 
#         return sorted(ToDo.instances.items()) 

# var1=ToDo('ckelele') 
# var1.give_priority(2) 
# var2=ToDo('lelelele') 
# var2.give_priority(3) 
# var3=ToDo('HIOHOHO')
# print('instances')


# class Parent: 
#     def __init__(self): 
#          pass 

#     def method(self): 
#          return 'Метод класса Parent' 

# class Child(Parent): 
#      pass 


# obj = Child() 
# print(obj.method()) 

# class Class1:
#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):
#     def fourth(self):
#         pass

#     def third(self):
#         pass

# obj = Class2()        
# obj.second()
# obj.first()
# obj.fourth()
# obj.third()


# class Transport: 
#      def move(self): 
#          print("движется:") 

# class Boat(Transport): 
#      def move(self): 
#          super().move() 
#          print("плывет") 

# class Car(Transport): 
#      def move(self): 
#          super().move()  
#          print("едет") 

# boat = Boat() 
# boat.move() 
# car = Car() 
# car.move() 

# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# class Number(int): 
#      def __init__(self, value): 
#          self.value = value
    
#      def count_digits(self): 
#          digits = len(str(self.value)) 
#          return digits 

# num = Number(123) 
# print(num.count_digits()) 



# class MyString(str): 
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
    
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
    
#     def pop(self): 
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w 
    
#     def __str__(self) -> str: 
#         return self.stroka1


# example = MyString('String') 
# example.append('hello') 
# print(example) 


# class MyList(list): 
#      def append(self, object): 
#          print('добавил!') 
#          return super().append(object) 

# lst = MyList([1, 2, 3]) 
# print(lst.append(4)) 
# print(lst)


# class MyDict(dict): 
    
#     def get(self,key,value = 'Are you kidding?'): 
#         return dict.get(self,key,value) 

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))



# def add(x, y): 
#     print(x + y) 

# add('makers ','bootcamp') 
# add([1, True], [3, False]) 
# add(1, 2)


# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# lst = [a, b, c]  
# for x in lst: 
#     print(len(x))


    
        
# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
    
#     @property 
#     def number(self): 
#         return self.__card_number 

# john = Person() 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)


# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
    
#     @property 
#     def number(self): 
#         return self.__card_number 
        
# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999") 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)



# def is_palindrome(str): 
#     if str.upper() == str.upper()[::-1]: 
#         return True 
#     else: 
#         return False 
# print(is_palindrome("sos"))

# def max_num(a, b):
#     return max(a, b)
# print(max_num(10, 12))



# f = open('text.txt')
# f.read()


# handle = open("test.txt", "r")
# for line in handle:
#     print(line)
# handle.close()




# import json
# json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


# import json
# json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# class Bag:
#     brand = 'GUCCHI'
#     def buy_bag(self, brand):
#         self.brand = brand
# bag1 = Bag()
# bag2 = Bag()
# bag1.buy_bag('CHANEL')
# print(bag1.brand)
# print(bag2.brand)


# class Lipstick:
#     color = 'red'
#     def set_color(self, color):
#         self.color = color
# Lipstick().set_color('pink')
# print(Lipstick().color)



# class ToDo:
#     instances = {}
    
#     def __init__(self, task):
#         self.task = task
           
#     def give_priority(self, priority):
#         self.instances[priority] = (self.task)

#     def list_of_tasks(self):
#         return sorted(ToDo.instances.items())

# obj = ToDo('to go to supermarket')
# obj.give_priority(2)
# print(obj.list_of_tasks())    
# print(obj.give_priority(2))
# us1 = ToDo('Сходить в школу')
# print(us1.task)
# us1.give_priority(1)
# print(ToDo.instances)
# us1 = ToDo('Поесть суши')
# us1.give_priority(3)
# print(ToDo.instances)
# print(us1.list_of_tasks())



# class Person:
   
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return  f'name:{self.name}, age:{self.age}' 
   
# class Student(Person):
#     def __init__(self, name, age, faculty):
#        self.faculty = faculty
#        super().__init__(name, age)

#     def display_student(self):
#         return  f'name:{self.name}, age:{self.age}, faculty:{self.faculty}' 

# obj_student = Student('Rick', '21', 'science')
# print(obj_student.display() )
# print(obj_student.display_student())


class GraphicalEntity:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.size_x = size_x
        self.size_y = size_y
class Button(GraphicalEntity):
    def __init__(self, pos_x, pos_y, size_x, size_y):
        super().__init__(pos_x, pos_y, size_x, size_y)
        self.status = False
def toggle(self):
    self.status = not self.status

class LimitSizeMixin:
    def __init__(self, pos_x, pos_y, size):
        size_x = min(size_x, 500)
        size_y = min(size_y, 400)
        super().__init__(pos_x, pos_y, size_x, size_y)

class LimitSizeButton(Button, LimitSizeMixin):
    pass
b = LimitSizeButton(10, 20, 200, 100)



























































































