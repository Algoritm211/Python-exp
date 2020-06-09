# - *- coding: utf- 8 - *-
import telebot
from telebot import types
import requests
import json
import datetime
import time
import requests
import apiinfo
import sqlite3
from collections import defaultdict
from threading import Timer
import clnews
import clmakegr
import warnings
import os
import sys
import psycopg2
from flask import Flask, request


WEBHOOK_SSL_CERT = './public.pem'
WEBHOOK_SSL_PRIV = './private.key'
PORT = 8443


warnings.filterwarnings('ignore')


'''Токен и время'''
TOKEN = '1070701499:AAHJH6wiCiN9BUj4MqnzpM6L46OXReF9fGs'
TIMEZONE = 'Europe/Kiev'
CURRENT_TIMEZONE = 'Kiev'
now = datetime.datetime.now()
DATABASE_URL = os.environ['postgresql-shallow-52252']
os.environ['postgresql-shallow-52252'] = 'postgres://mstsdlykkfafbz:92d6171ebfedd9fa2b493c970dacd0c66f711ca0e9a287ba031844b3a5a65038@ec2-3-229-210-93.compute-1.amazonaws.com:5432/d8osekavt32nmq'
bot = telebot.TeleBot(TOKEN, threaded=False)
bot.remove_webhook()
URL='https://afternoon-ridge-23028.herokuapp.com:'+str(PORT)
# URL = 'https://82.193.126.240:' + str(PORT)
bot.set_webhook(url=URL, certificate=open(WEBHOOK_SSL_CERT, 'rb'))
'''Клавиатура'''
keyboard_1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_1.row('BTC info', 'ETH info', 'XRP info')
'''база данных'''

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()
create_table_btc = """CREATE TABLE IF NOT EXISTS Cryptobot
                    (Bitcoin char(50) NOT NULL,
                    Ethereum char(50) NOT NULL,
                    XRP char(50) NOT NULL,
                    "date" char(10) NOT NULL);"""
cursor.execute(create_table_btc)
conn.commit()
create_table_user = """CREATE TABLE IF NOT EXISTS Userinfo ("user_id" char(50) NOT NULL);"""
cursor.execute(create_table_user)
conn.commit()
'''Для уведомлений'''
done = False


'''WEBHOOK'''

app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

'''Выполнение команд'''
@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, '🤖Здравствуйте, '+ message.from_user.first_name + '!\n' \
    '💵Я могу показать Вам цены и графики цифровых активов, а также рассказать о последних новостях в сфере криптовалют \n' +
    '💰Для просмотра инструкции пользователя нажмите /help.\n\n\n'+
    'Powered by Alexey Horbunov\n'+
    '@Alexey_Horbunov', reply_markup=keyboard_1)

    def update_crypto_price():
        Timer(43200, update_crypto_price).start()
        update_cryptos = """INSERT INTO Cryptobot(Bitcoin, Ethereum, XRP, "date")
        SELECT %s, %s, %s, %s
        WHERE NOT EXISTS (
        SELECT * FROM Cryptobot WHERE "date" = %s );"""
        cursor.execute(update_cryptos, (apiinfo.get_btc(), apiinfo.get_eth(), apiinfo.get_xrp(), now.strftime("%d-%m-%Y"), now.strftime("%d-%m-%Y")))
        conn.commit()
    update_crypto_price()


@bot.message_handler(commands=['help'])
def message_help(message):
    markup_author = types.InlineKeyboardMarkup(row_width=1)
    item_author = types.InlineKeyboardButton('Об авторе бота', callback_data='author')
    markup_author.add(item_author)
    bot.send_message(message.chat.id, '❓Итак, в настоящий момент бот имеет такие функции: \n' +
    '1️⃣) Вы можете узнать текущую цену криптовалют нажав команду /exchange и выбрав интересующую вас криптовалюту\n'+
    '2️⃣) Вы можете просмотреть цену конкретной криптовалюты с крупнейшей '+
     'биржи Binance воспользовавшись кнопками снизу, а также после промотреть ее график, а также перейти на биржу🔶', reply_markup=markup_author)

@bot.message_handler(commands=['exchange'])
def propose_cryptos(message):
    bot.send_message(message.chat.id, 'Выберите криптовалюту, цену которой хотели бы получить: ', reply_markup = keyboard_1)

@bot.message_handler(commands=['news'])
def propose_news(message):
    markup_news = types.InlineKeyboardMarkup(row_width=1)
    item1_news = types.InlineKeyboardButton('Bitexpert', callback_data='btcxpert')
    item2_news = types.InlineKeyboardButton('Forklog', callback_data='forklog')
    item3_news = types.InlineKeyboardButton('Coinspot', callback_data='coinspot')
    markup_news.add(item1_news, item2_news, item3_news)
    bot.send_message(message.chat.id, '📰Выберите источник, с которого хотели бы получить новости: ', reply_markup=markup_news)


@bot.message_handler(content_types=['text'])
def give_cryptos(message):
    markup1 = types.InlineKeyboardMarkup(row_width=1)
    item1_1 = types.InlineKeyboardButton('📊Показать график BTC', callback_data='grbtc')
    item1_2 = types.InlineKeyboardButton(text="🔶Перейти на Binance", url="https://www.binance.com/en/trade/BTC_USDT")
    markup1.add(item1_1, item1_2)

    markup2 = types.InlineKeyboardMarkup(row_width=1)
    item2_1 = types.InlineKeyboardButton('📊Показать график ETH', callback_data='greth')
    item2_2 = types.InlineKeyboardButton(text="🔶Перейти на Binance", url="https://www.binance.com/en/trade/ETH_USDT")
    markup2.add(item2_1, item2_2)

    markup3 = types.InlineKeyboardMarkup(row_width=1)
    item3_1 = types.InlineKeyboardButton('📊Показать график XRP', callback_data='grxrp')
    item3_2 = types.InlineKeyboardButton(text="🔶Перейти на Binance", url="https://www.binance.com/en/trade/XRP_USDT")
    markup3.add(item3_1, item3_2)


    if message.text.lower() == 'btc info':
        bot.send_message(message.chat.id, 'ℹЗагружаю актуальную информацию...........')
        res = message.text[:3]
        price_usd = apiinfo.get_btc()
        bot.send_message(message.chat.id,
        '🚩 BITCOIN INFO 🚩\n'+
        '📄 Информация с биржи 🔸Binance🔸\n'+
        'Пара 🔹BTC-USDT🔹 📄\n'+
        '💰' + price_usd +'\n',reply_markup=markup1)

    elif message.text.lower() == 'eth info':
        bot.send_message(message.chat.id, 'ℹЗагружаю актуальную информацию...........')
        res = message.text[:3]
        price_usd = apiinfo.get_eth()
        bot.send_message(message.chat.id,
        '🚩 ETHEREUM INFO 🚩\n'+
        '📄 Информация с биржи 🔸Binance🔸\n'+
        'Пара 🔹ETH-USDT🔹 📄\n'+
        '💰' + price_usd +'\n',reply_markup=markup2)

    elif message.text.lower() == 'xrp info':
        bot.send_message(message.chat.id, 'ℹЗагружаю актуальную информацию...........')
        res = message.text[:3]
        price_usd = apiinfo.get_xrp()
        bot.send_message(message.chat.id,
        '🚩 XRP INFO 🚩\n'+
        '📄 Информация с биржи 🔸Binance🔸\n'+
        'Пара 🔹XRP-USDT🔹 📄\n'+
        '💰' + price_usd +'\n',reply_markup=markup3)

    else:
        bot.send_message(message.chat.id, '‼Что-то пошло не так или я не знаю такой команды.' +
        'Нажмите на одну из предложенных кнопок или узнайте о функциях бота с помощью команды /help‼')
'''
    if done:
        def timed_job():
            Timer(10, timed_job).start()
            high = 9600
            low = 9400
            price_usd = float(apiinfo.get_btc())
            if price_usd >= high:
                bot.send_message(message.chat.id, text= 'БОЛЬШЕ ВЕРХНЕЙ ТОЧКИ')
            if price_usd <= high:
                bot.send_message(message.chat.id, text= 'МЕНЬШЕ НИЖНЕЙ ТОЧКИ')

        timed_job()
'''

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        markup_go_to_bitexpert = types.InlineKeyboardMarkup(row_width=1)
        item_bitexpert = types.InlineKeyboardButton('➡Перейти на Bitexpert.io➡', url='https://bitexpert.io')
        markup_go_to_bitexpert.add(item_bitexpert)

        markup_go_to_coinspot = types.InlineKeyboardMarkup(row_width=1)
        item_coinspot = types.InlineKeyboardButton('➡Перейти на Coinspot.io➡', url='https://coinspot.io')
        markup_go_to_coinspot.add(item_coinspot)

        markup_go_to_forklog = types.InlineKeyboardMarkup(row_width=1)
        item_forklog = types.InlineKeyboardButton('➡Перейти на Forklog.com➡', url='https://forklog.com')
        markup_go_to_forklog.add(item_forklog)
        if call.data == 'grbtc':
            clmakegr.get_gr_btc()
            gr = open('GRbtc.png', 'rb')
            bot.send_photo(call.message.chat.id, gr, reply_markup=keyboard_1)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ваш график")
            os.remove('GRbtc.png')
        elif call.data == 'greth':
            clmakegr.get_gr_eth()
            gr = open('GReth.png', 'rb')
            bot.send_photo(call.message.chat.id, gr, reply_markup=keyboard_1)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ваш график")
            os.remove('GReth.png')
        elif call.data == 'grxrp':
            clmakegr.get_gr_xrp()
            gr = open('GRxrp.png', 'rb')
            bot.send_photo(call.message.chat.id, gr, reply_markup=keyboard_1)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ваш график")
            os.remove('GRxrp.png')
        elif call.data == 'author':
            photo_creator = open('MRZ.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo_creator,'<b>Привет, меня зовут Алексей Горбунов и я создатель этого бота😎</b>\n\n'+
            'В настоящий момент я студет КПИ, увелекаюсь программированием на Python, вместе с этим работаю журналистом на портале Bitexpert.io\n'+
            'Люблю учиться и открыт всему новому\n\n'+
            '<i>С удовольствием рассмотрю все ваши предложения, а также замечания по поводу моего бота</i>\n'+
            'Отвечу на все вопросы в телеграме - @Alexey_Horbunov, а также на почту algoritm211@gmail.com\n\n'+
            'P.S. На фото мой кот Мурзак)', parse_mode='HTML', reply_markup=keyboard_1)

        elif call.data == 'btcxpert' or 'forklog' or 'coinspot':
            if call.data == 'btcxpert':
                data_news_bitexpert = clnews.get_news_bitexpert_io()
                bot.send_message(call.message.chat.id, text='----------\n' + '📍<b>Последние новости на Bitexpert.io</b>📍\n' + '----------\n' + \
                                                            data_news_bitexpert, parse_mode='HTML', reply_markup=markup_go_to_bitexpert)
            if call.data == 'forklog':
                data_news_forklog = clnews.get_news_forklog_com()
                bot.send_message(call.message.chat.id, text='----------\n' + '📍<b>Последние новости на Forklog.com</b>📍\n' + '----------\n' + \
                                                            data_news_forklog, parse_mode='HTML', reply_markup=markup_go_to_forklog)

            if call.data == 'coinspot':
                data_news_coinspot = clnews.get_news_coinspot_io()
                bot.send_message(call.message.chat.id, text='----------\n' + '📍<b>Последние новости на Coinspot.io</b>📍\n' + '----------\n' + \
                                                            data_news_coinspot, parse_mode='HTML', reply_markup=markup_go_to_coinspot)





'''running'''
# bot.polling(none_stop=True)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV), debug = False)
