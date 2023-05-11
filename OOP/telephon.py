class MobilePhone:
    _battery=100 

    def __init__(self, imei, os_info) -> None:
        self._imei = imei
        self._os_info = os_info

    def info(self):
        if self._battery == 0:
            return f'Телефон разряжен. Зарядите телефон'    
        elif self._battery >= 0:
            if self._battery == 0.5:
                self._battery -= 0.5
                return f'Телефон имеет imei: {self._imei} и на нем установлена ОС: {self._os_info}.\nОстаток заряда составляет: {self._battery}%.\nЗарядите телефон'
            else:
                self._battery -= 0.5
                return f'Телефон имеет imei: {self._imei} и на нем установлена ОС: {self._os_info}.\nОстаток заряда составляет: {self._battery}%'
          
    def listening_to_music(self):
        if self._battery > 0:
            if self._battery < 5:
                return f'Вы более не можете слушать музыку. Простите. Зарядите телефон.'
            elif self._battery == 5:
                self._battery -= 5
                return f'Вы прослушали музыку, но телефон уже разрядился. Заряд батареи: {self._battery}%.\nЗарядите телефон'
            else:
                self._battery -= 5
                return f'Приятного прослушивания музыки. Заряд батареи: {self._battery}%'
        else:
            return f'Телефон разряжен. Зарядите телефон'

    def watching_video(self):
        if self._battery > 0:
            if self._battery > 10:
                self._battery -= 7
                return f'Приятного просмотра видео. Заряд батареи: {self._battery}%'
            else:
                return f'Уровень заряда батареи составляет {self._battery}%. При таком заряде нельзя просматривать видео. Зарядите телефон'
        else:
            return f'Телефон разряжен. Зарядите его'
        
    def charge(self):
        import time

        count_time = 0
        while self._battery < 100:
            if self._battery > 90:
                self._battery += 100 - self._battery
            else:
                self._battery += 10           
            time.sleep(1)
            count_time += 1
            print(f'За {count_time} сек заряд составил {self._battery}%')
        
iphone = MobilePhone('wewe3', 'iOs')
print(iphone.listening_to_music())
print(iphone.listening_to_music())
print(iphone.listening_to_music())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.watching_video())
print(iphone.listening_to_music())
# print(iphone.listening_to_music())
# print(iphone.listening_to_music())
# print(iphone.listening_to_music())
# # iphone.charge()
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
# print(iphone.info())
iphone.charge()
print(iphone.watching_video())