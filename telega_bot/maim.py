# import telebot
# from telebot import types
# import random

# token = '6184082580:AAED8O9jnH6Fjw2QkCDwJ3HAA1qm4n7vis4'

# bot = telebot.TeleBot(token)

# keyboard = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton('Играть!')
# btn2 = types.KeyboardButton('Нет, я Пас!')
# keyboard.add(btn1,btn2)



# @bot.message_handler(commands=['start', 'game'])
# def start_message(message):
#     bot_message = bot.send_message(message.chat.id, 'Привет King, начнём игру?', reply_markup=keyboard)
#     bot.register_next_step_handler(bot_message, check_answer)

# def check_answer(message):
#     if message.text == 'Играть!':
#         bot.send_message(message.chat.id, 'Ok тогда лови правила игры\nНужно угодать число которое я загодаю в диапазоне от 1 до 10 включительно! У тебя будет три попытки!! Если не угодаешь я тебя пристрелю!!! :)')
#         number = random.randint(1, 10)
#         print(number,'!!!!')
#         game(message, 3, number)
#     elif message.text == 'Нет, я Пас!':
#         bot.send_message(message.chat.id, 'Net tak Net, Poka!!')
#     else:
#         bot_message = bot.send_message(message.chat.id, 'Вы ввели не правельный ответ!!!\nВведите новый!!:',reply_markup=keyboard)
        
#         bot.register_next_step_handler(bot_message, check_answer)


# def game(message, attempts, number):
#     message_bot = bot.send_message(message.chat.id, 'Выбери число:')
#     bot.register_next_step_handler(message_bot, check_number, attempts-1, number)


# def check_number(message, attempts, number):
#     if message.text == str(number):
#         bot.send_message(message.chat.id, 'Вы победили!!! Нарекаю Вас удачлевым!!')
#     elif attempts == 0:
#         bot.send_message(message.chat.id, 'Ты проиграл!!! Иди поучись на заднем дворе!!')
#     else:
#         bot.send_message(message.chat.id, 'Нет ты не угодал число, попробуй ещё раз!')
#         game(message, attempts, number)




# bot.polling()







# import telebot
# from telebot import types
# from bs4 import BeautifulSoup
# from requests import get
# # from my_token import token

# bot = telebot.TeleBot('6184082580:AAED8O9jnH6Fjw2QkCDwJ3HAA1qm4n7vis4')

# markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# btn1 = types.KeyboardButton('/start')
# markup.add(btn1)

# @bot.message_handler(commands=['start', 'text'])
# def start_message(message):
#     chat_id = message.chat.id
#     msg = bot.send_message(chat_id, 'Давай послушаем музыку!\nВведи название исполнителя или композицию', reply_markup=markup)
#     bot.register_next_step_handler(msg, find_the_song)
    
# def find_the_song(message):
#     url = f'https://zaycev.net/search.html?query_search={message.text}'
#     html = get_html(url)
#     soup = get_soup(html)
#     try:
#         singerMain = soup.find('div', class_='sc-1ivpr86-3 dcizwQ').find('ul', class_='sc-18st3ox-1 eKEXNL')
#     except:
#         chat_id = message.chat.id
#         bot.send_message(chat_id, 'Ничего не нашли. Уточните исполнителя или композицию.')
#         start_message(message)
#         return
#     else:
#         all_songs = get_data_songs(singerMain)
#         chat_id = message.chat.id
#         msg_list = []
#         for i in all_songs:
#             art = i['artist']
#             name = i['name']
#             link = i['url']
#             msg = f'Название: "{name}"\nАртист: "{art}"\nCсылка {link}\n\n'
#             msg_list.append(msg)
#         all_msg = ''.join(msg_list)
#         bot.send_message(chat_id, all_msg)

# def get_html(url: str) -> str:
#     '''Эта функция получает HTML разметку по определенному сайту по URL'''
#     response = get(url)
#     return response.text

# def get_soup(html: str) -> BeautifulSoup:
#     ''' Получает html разметку и структурирует ее в красивый bs'''
#     soup = BeautifulSoup(html, 'lxml')
#     return soup

# def get_data_songs(singerMain):
#     res_search = []
#     singer = singerMain.find_all('li')
#     for item in singer:
#         song_art = item.find('div', class_='sc-1cisiq-6 gmCfCb').text
#         song_name = item.find('div', class_='fa9swr-6 eOPoOa').find('a', class_='sc-1vuj2t8-0 pbfhi').text
#         song_url = 'https://zaycev.net'+item.find('div', class_='fa9swr-6 eOPoOa').find('a', class_='sc-1vuj2t8-0 pbfhi').get('href')
#         data = {
#                 'artist': song_art,
#                 'name': song_name,
#                 'url': song_url
#             }
#         res_search.append(data)
    
#     return res_search

# def no_search_result(message):
#     chat_id = message.chat.id
#     msg = bot.send_message(chat_id, 'Нет такой композиции или исполнителя. Во всяком случае мы не нашли. Уточни запрос. Начнем сначала!')
#     start_message()

# bot.polling(none_stop=True, interval=0)
















































































































































































































