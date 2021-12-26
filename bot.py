import requests as r
from requests.auth import HTTPBasicAuth
import telebot
import time
from telebot import types

bot = telebot.TeleBot('5065414273:AAG2iuFSLUjeKAq2TEQ5ttsncaN3xVQY5i4')

""""
class CheckMethod:
    def __init__(self):
        self.running = None

    def set_running(self, running):
        self.running = running

    def get_running(self):
        return self.running
"""


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn = types.KeyboardButton('Получи котов')
    markup.add(btn)
    bot.reply_to(message, "Привет, нажми на кнопку нижу и получи котов", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_cat(message):
    def cats_going():
        response = r.get('https://api.thecatapi.com/v1/images/search',
                         auth=HTTPBasicAuth('user', 'a0a6a2d5-d7dd-4341-ac89-3cdbcce6531d'))
        image = response.json()
        for url in image:
            get = url["url"]
            bot.send_message(message.chat.id, get)

    def stop_this_fucking_cats():
        markup1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton('Получи котов')
        markup1.add(btn1)
        bot.reply_to(message, "Ты же хочешь еще котов?",
                     reply_markup=markup1)

    if message.text == 'Получи котов':
        cats_going()
        stop_this_fucking_cats()

"""
    a = CheckMethod()
    a.set_running(1)
    while a.get_running() == 1:
        if message.text == "Стоп":
            markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
            btn = types.KeyboardButton('Получи котов')
            markup.add(btn)
            bot.reply_to(message, "Ты остановил, нажми на кнопку чтобы опять вернуть себе котов",
                         reply_markup=markup)
            a.set_running(3)
        elif message.text == 'Получи котов':
            #time.sleep(5)
            response = r.get('https://api.thecatapi.com/v1/images/search',
                             auth=HTTPBasicAuth('user', 'a0a6a2d5-d7dd-4341-ac89-3cdbcce6531d'))
            image = response.json()
            for url in image:
                get = url["url"]
                bot.send_message(message.chat.id, get)
"""

"""
    @bot.message_handler(content_types=['text'])
    def after_error(message):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
        btn = types.KeyboardButton('Получи котов')
        markup.add(btn)
        bot.reply_to(message, "Ты остановил, нажми на кнопку чтобы опять вернуть себе котов",
                     reply_markup=markup)
"""


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
