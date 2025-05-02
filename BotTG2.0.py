import random
import telebot 
from telebot import types
import os
import schedule
from threading import Thread
from time import sleep

folder_dir = 'pic'

file = open('support.txt', 'r', encoding='utf-8')
support = file.read().split('\n')
file.close()

file = open('stic.txt', 'r', encoding='utf-8')
stic = file.read().split('\n')
file.close()

bot = telebot.TeleBot('Введи Токен')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Я устал...😞')
    item2 = types.KeyboardButton('Я за***лся!😫')
    item3 = types.KeyboardButton('Кто тебя создал?')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Как ты, дружище?💜', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_handle_text(message):

    if  message.text.strip() == 'Я устал...😞':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Ну, спасибо тебе👍🏽')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Ной не ныл, и ты не ной!😌', reply_markup=markup)
        user_id = message.from_user.id
        def function_to_run():
            bot.send_message(user_id, random.choice(support))
        schedule.every(1).minutes.do(function_to_run)
    elif message.text.strip() == 'Ну, спасибо тебе👍🏽':
        stickers = str(random.choice(stic))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Я устал...😞')
        item2 = types.KeyboardButton('Я за***лся!😫')
        item3 = types.KeyboardButton('Кто тебя создал?')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Очень рад за тебя! Так держать😁👍🏽', reply_markup=markup)
        bot.send_sticker(message.chat.id, stickers)
        schedule.clear()
    elif message.text.strip() == 'Я за***лся!😫':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Все, отпустило!👍🏽')
        markup.add(item1)
        bot.send_message(message.chat.id, 'Может поработаешь?!😡', reply_markup=markup)
        user_id = message.from_user.id
        def function_to_run():
            bot.send_message(user_id, random.choice(support))
        schedule.every(1).minutes.do(function_to_run)
    elif message.text.strip() == 'Все, отпустило!👍🏽':
        stickers = str(random.choice(stic))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Я устал...😞')
        item2 = types.KeyboardButton('Я за***лся!😫')
        item3 = types.KeyboardButton('Кто тебя создал?')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Красавчик! В бой!😁👍🏽', reply_markup=markup)
        bot.send_sticker(message.chat.id, stickers)
        schedule.clear()
    elif message.text.strip() == 'Кто тебя создал?':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Сайт-визитка', url='https://kovalenkoli.github.io/')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Уверен, что тебе это интересно?☺ Переходи по ссылке!'.format(message.from_user), reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Ой... кажется, я еще не умею читать сообщения с клавиатуры😥 Если хочешь написать мне, жми по кнопкам моего меню😊')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEMszhitv7mZurHw02jOtUsHXmO9O84-QACDxUAAlAAATlItNCNfsmsILopBA')


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)


Thread(target=schedule_checker).start()


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
