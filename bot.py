import requests as r
from requests.auth import HTTPBasicAuth
import telebot
from telebot import types
from quotes import tags, help_txt
from random import choice

bot = telebot.TeleBot('token')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Хочу кота 🙀')
    btn2 = types.KeyboardButton('Я панікую')
    markup.add(btn1, btn2)
    bot.reply_to(message, "Привіт, натисни на кнопку \nотримай кота та заспокой свою душу хоча б на трохи",
                 reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_cat(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton('Хочу кота 🙀')
    btn2 = types.KeyboardButton('Я панікую')
    markup.add(btn1, btn2)

    def cats_going():
        response = r.get('https://api.thecatapi.com/v1/images/search',
                         auth=HTTPBasicAuth('user', 'a0a6a2d5-d7dd-4341-ac89-3cdbcce6531d'))
        image = response.json()
        for url in image:
            get = url["url"]
            bot.send_message(message.chat.id, get)
        item = choice(tags)
        bot.send_message(message.chat.id, item, reply_markup=markup)

    if message.text == 'Хочу кота 🙀':
        cats_going()
    if message.text == "Я панікую":
        bot.send_message(message.chat.id, help_txt, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
