
import telebot
from telebot import types


bot = telebot.TeleBot('7460135326:AAEFdeakpaJirCHvoEmYXeFQJjMJPpuaby4')
@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)