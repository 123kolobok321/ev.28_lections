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
       












