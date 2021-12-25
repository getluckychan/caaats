import requests as r
from requests.auth import HTTPBasicAuth
import telebot
import time
from telebot import types


bot = telebot.TeleBot('5065414273:AAG2iuFSLUjeKAq2TEQ5ttsncaN3xVQY5i4')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я буду отправлять тебе котов каждые 3 минуты"
                          "\nнажми /cats чтобы начать")


@bot.message_handler(commands=['cats'], content_types=['text'])
def get_cat(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn = types.KeyboardButton('Стоп')
    markup.add(btn)
    bot.reply_to(message, "Нажми на кнопку чтобы остановить", reply_markup=markup)
    while True:
        response = r.get('https://api.thecatapi.com/v1/images/search',
                         auth=HTTPBasicAuth('user', 'a0a6a2d5-d7dd-4341-ac89-3cdbcce6531d'))
        image = response.json()
        if response.status_code == 200:
            for url in image:
                get = url["url"]
                bot.send_message(message.chat.id, get)
                time.sleep(180)
        if message.text == "Стоп":
            bot.reply_to(message, "Ты остановил рассылку, нажми /cats чтобы снова начать")
            break


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
