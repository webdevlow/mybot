# -*- coding: utf-8 -*-
import telebot
from telebot import types
import sqlite3
from sqlite3 import Error
from time import sleep, ctime
import random
from random import randint
import requests
from requests import get
import time

# тут токен бота
bot = telebot.TeleBot("5501287517:AAE4wq7Hcn1lAPvLNDskEUpuDBNNeX4Qm9A")

# переменные с данными
supportid = ""
tokenqiwi = ""
numberqiwi = ""
admin = 5223030160
password = "3331"

list1 = ["Название: 😼 Мини 99₽ Скидка 32%🔥", "Название: 👧🏼 Юные создания 10-16 💧 ЦЕНА: 149₽", "Название: ❤️ lllкоLьные Секс 12-16 😜 ЦЕНА: 199₽",
					"Название: 👨‍👩‍👧‍👦 ИNСЕSТЫ 👨‍👩‍👧‍👦 ЦЕНА: 219₽ [-50%]", "Название: 👧🏻 Мега Приват 👧🏻 ЦЕНА: 299₽", "Название: 🍌САМАЯ Жесть🍌 ЦЕНА: 415₽",
					"Название: 🤑Все включено🤑 ЦЕНА: 450₽ [-35%]", "Название: 🥵 UZНОСЫ 🥵 ЦЕНА: 435₽ [-50%]", "Название: 🔞 FULL BIG PACK 🍭 ЦЕНА: 650₽", "Название: ✅ PORNHUB PREMIUM ACCOUNT ✅ ЦЕНА: 49₽", "💕 Sекс брата и сестры 16 years 💕"]


# создание и подключение к бд
def post_sql_query(sql_query):
	with sqlite3.connect('hugoboss.db') as connection:
		cursor = connection.cursor()
		try:
			cursor.execute(sql_query)
		except Error:
			pass
		result = cursor.fetchall()
		return result




def create_tables():
	users_query = '''CREATE TABLE IF NOT EXISTS USERS 
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        reg_date TEXT);'''
	post_sql_query(users_query)

def register_user(user, username, first_name, last_name):
	user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
	user_check_data = post_sql_query(user_check_query)
	if not user_check_data:
		insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
		post_sql_query(insert_to_db_query )
		print("новый юзер! ")

create_tables()

@bot.message_handler(commands=['start'])
def start_message(message):
	markup_reply = telebot.types.InlineKeyboardMarkup()
	markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Тюмень', callback_data=1))
	markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Екатеринбург', callback_data=2))

	register_user(message.from_user.id, message.from_user.username,
	              message.from_user.first_name, message.from_user.last_name)
	familiya = message.from_user.last_name
	

	bot.send_photo(message.chat.id, get(f"https://i.ibb.co/qjN09JP/photo-2022-05-26-18-31-55.jpg").content)
	bot.send_message(message.chat.id, 
											f'<b>Приветствуем, тебя в Магазине HUGO BOSS SHOP 🙌</b>\n'
											f'В нашем магазине всегда свежие адреса и отличное качество товара. 💎\n'
											f'Перед совершением покупки просим ознакомиться с правилами магазина. 👑\n\n'
											f'<b>/start - меню магазина\n\n</b>'
											f'<b>✅ ВНИМАНИЕ! ОСТЕРЕГАЙТЕСЬ МОШЕННИКОВ! ТОЛЬКО ЭТОТ БОТ ОРИГИНАЛЬНЫЙ!</b>\n'
											f'Мы торгуем только Мефедроном!\n\n'
											f'Будьте уверены в том, что мы тот самый HUGO BOSS SHOP - Свяжитесь с нами по Контактам ниже 👌\n\n'
											f'<b><i>Отзывы на нашем сайте</i></b>\n\n'
											f'<i>Мы будем рады получить обратную связь по качеству продукта/работе магазина/предпочтительным районам</i>\n\n'
											f'<b>Наши контакты:</b>\n'
											f'<b>👇 Клирнет</b>\n'
											f'<b>hugoboss.biz</b>\n'
											f'<b>👇 Onion</b>\n'
											f'<b>3k3wg4ixmguqjlufh6fpwnic6i56hq4jipxwnha675jflj64hnysnaad.onion</b>\n'
											f'<b>👇 OMG Маркетплейс</b>\n'
											f'<b>omgomgomg5j4yrr4mjdv3h5c5xfvxtqqs2in7smi65mjps7wvkmqmtqd.onion/shop/items/57373982-2887-4c25-83cd-6c986c32b6ce</b>\n'
											f'<b>👇 BlackSprut Маркетплейс</b>\n'
											f'<b>blackvcvv4cpsaurawnw7p5yazwfi6djlc77sfgzinexj4ilkmprr2qd.onion/stores/1025</b>\n'
											f'<b>👇Наша ветка на Rutor</b>\n'
											f'<b>http://rutordeepkpafpudl22pbbhzm4llbgncunvgcc66kax55sc4mp4kxcid.onion/threads/hugo-boss-mefedron-opt-i-roznica-ekaterinburg-tjumen.50011</b>', parse_mode='html', reply_markup=markup_reply)


# обработка callback клавиатуры
@bot.callback_query_handler(func=lambda message: True)
def KeyboardInline(call):
	register_user(call.message.from_user.id, call.message.from_user.username,
	              call.message.from_user.first_name, call.message.from_user.last_name)
	if call.data == '1':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Мефедрон Мука | 1 грамм', callback_data='mef1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Мефедрон Мука | 2 грамм', callback_data='mef2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Мефедрон Мука | 3 грамм', callback_data='mef3'))
		bot.send_message(call.message.chat.id, "Выберите товар:", reply_markup = markup_reply)

	if call.data == '2':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Мефедрон Кристалл | 1 грамм', callback_data='mef1ekb'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Мефедрон Кристалл | 2 грамм', callback_data='mef2ekb'))
		bot.send_message(call.message.chat.id, "Выберите товар:", reply_markup = markup_reply)

		#TYUMENTYUMEN
	if call.data == 'mef1':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Войновка | Тайник', callback_data='mef1tmn'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Центр | Тайник', callback_data='mef2tmn'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 ММС | Тайник', callback_data='mef3tmn'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Ленинский район | Тайник', callback_data='mef4tmn'))
		bot.send_message(call.message.chat.id, "Выберите район: ", reply_markup = markup_reply)
	if call.data == 'mef2':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Войновка | Тайник', callback_data='mef1tmn2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 ММС | Тайник', callback_data='mef2tmn2'))
		bot.send_message(call.message.chat.id, "Выберите район: ", reply_markup = markup_reply)
	if call.data == 'mef3':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Гилёвская роща | Тайник', callback_data='mef1tmn3'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 ММС | Тайник', callback_data='mef3tmn3'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Бабарынка | Тайник', callback_data='mef4tmn3'))
		bot.send_message(call.message.chat.id, "Выберите район: ", reply_markup = markup_reply)

		#EKBEKBEKB
	if call.data == 'mef1ekb':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Верх-Исетский | Тайник', callback_data='mef1ekb1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Юго-Западный | Тайник', callback_data='mef2ekb1'))
		bot.send_message(call.message.chat.id, "Выберите район: ", reply_markup = markup_reply)

	if call.data == 'mef2ekb':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Пионерский (город) | Тайник', callback_data='mef1ekb2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔶 Уктус | Тайник', callback_data='mef2ekb2'))
		bot.send_message(call.message.chat.id, "Выберите район: ", reply_markup = markup_reply)


	#при выборе района на 1г тмн
	if call.data == 'mef1tmn':
		randomstaff = random.randint(2, 3)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Войновка | Тайник</b>\n\nЦена: <b>2200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef2tmn':
		randomstaff = random.randint(3, 4)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Центр | Тайник</b>\n\nЦена: <b>2200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef3tmn':
		randomstaff = random.randint(4, 5)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>ММС | Тайник</b>\n\nЦена: <b>2200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef4tmn':
		randomstaff = random.randint(5, 6)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Ленинский район | Тайник</b>\n\nЦена: <b>2200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)

	#при выборе района на 2г тмн

	if call.data == 'mef1tmn2':
		randomstaff = random.randint(3, 4)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Войновка | Тайник</b>\n\nЦена: <b>3999руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef2tmn2':
		randomstaff = random.randint(5, 6)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>ММС | Тайник</b>\n\nЦена: <b>3999руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)

	#при выборе района на 3г тмн


	if call.data == 'mef1tmn3':
		randomstaff = random.randint(1, 3)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy3'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Гилёвская Роща | Тайник</b>\n\nЦена: <b>5650руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef3tmn3':
		randomstaff = random.randint(5, 6)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy3'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>ММС | Тайник</b>\n\nЦена: <b>5650руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)

	if call.data == 'mef4tmn3':
		randomstaff = random.randint(7, 8)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buy3'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Бабарынка | Тайник</b>\n\nЦена: <b>5650руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	#при выборе района на 1г екб

	if call.data == 'mef1ekb1':
		randomstaff = random.randint(5, 6)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buyekb1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Верх-Исетский район | Тайник</b>\n\nЦена: <b>2650руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef2ekb1':
		randomstaff = random.randint(3, 4)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buyekb1'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Юго-Западный | Тайник</b>\n\nЦена: <b>2650руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)

	#при выборе района на 2г екб

	if call.data == 'mef1ekb2':
		randomstaff = random.randint(5, 6)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buyekb2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Пионерский район (город) | Тайник</b>\n\nЦена: <b>5200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)
	if call.data == 'mef2ekb2':
		randomstaff = random.randint(3, 4)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='💰 Купить', callback_data='buyekb2'))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='🔙 Назад', callback_data='back'))
		bot.send_message(call.message.chat.id, f"Вы выбрали <b>Уктус | Тайник</b>\n\nЦена: <b>5200руб.</b>\nКоличество на складе: <b>{randomstaff}</b>", parse_mode='html', reply_markup=markup_reply)




		# ПОКУПКА МЕФ ТМН 1
	if call.data == 'buy1':
		zakaz = random.randint(2300, 5000)
		randommoney = random.randint (2450, 2480)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='back'))
		bot.send_message(call.message.chat.id, f"<b>Создан заказ #{zakaz}</b>\n\n<b>Тюмень | Мефедрон 1гр. Тайник</b>\n\n💶 Переведите <b>{randommoney} RUB</b>\n💳 Реквизиты для оплаты: <b>4890 4947 3261 6792</b>\n\nРеквизиты действительны ровно 30 минут, если не успеваете оплатить, пересоздайте сделку, иначе рискуете потерять деньги.\n<b>ВНИМАНИЕ!</b>  Сверяйте номер заказа и реквизиты по которым оплачиваете! Точная сумма, верные реквизиты, иначе рискуете потерять деньги. Если вы оплачиваете через BTC, то автоматическая выдача происходит после 2х подтверждений.", parse_mode='html', reply_markup=markup_reply)	


		# ПОКУПКА МЕФ ТМН 2

	if call.data == 'buy2':
		zakaz = random.randint(2300, 5000)
		randommoney = random.randint (4401, 4459)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='back'))
		bot.send_message(call.message.chat.id, f"<b>Создан заказ #{zakaz}</b>\n\n<b>Тюмень | Мефедрон 2гр. Тайник</b>\n\n💶 Переведите <b>{randommoney} RUB</b>\n💳 Реквизиты для оплаты: <b>4890 4947 3261 6792</b>\n\nРеквизиты действительны ровно 30 минут, если не успеваете оплатить, пересоздайте сделку, иначе рискуете потерять деньги.\n<b>ВНИМАНИЕ!</b>  Сверяйте номер заказа и реквизиты по которым оплачиваете! Точная сумма, верные реквизиты, иначе рискуете потерять деньги. Если вы оплачиваете через BTC, то автоматическая выдача происходит после 2х подтверждений.", parse_mode='html', reply_markup=markup_reply)	

		# ПОКУПКА МЕФ ТМН 3

	if call.data == 'buy3':
		zakaz = random.randint(2300, 5000)
		randommoney = random.randint (6251, 6259)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='back'))
		bot.send_message(call.message.chat.id, f"<b>Создан заказ #{zakaz}</b>\n\n<b>Тюмень | Мефедрон 3гр. Тайник</b>\n\n💶 Переведите <b>{randommoney} RUB</b>\n💳 Реквизиты для оплаты: <b>4890 4947 3261 6792</b>\n\nРеквизиты действительны ровно 30 минут, если не успеваете оплатить, пересоздайте сделку, иначе рискуете потерять деньги.\n<b>ВНИМАНИЕ!</b>  Сверяйте номер заказа и реквизиты по которым оплачиваете! Точная сумма, верные реквизиты, иначе рискуете потерять деньги. Если вы оплачиваете через BTC, то автоматическая выдача происходит после 2х подтверждений.", parse_mode='html', reply_markup=markup_reply)	


		# ПОКУПКА МЕФ ЕКБ 1 

	if call.data == 'buyekb1':
		zakaz = random.randint(2300, 5000)
		randommoney = random.randint (3020, 3050)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='back'))
		bot.send_message(call.message.chat.id, f"<b>Создан заказ #{zakaz}</b>\n\n<b>Екатеринбург | Мефедрон Кристалл 1гр. Тайник</b>\n\n💶 Переведите <b>{randommoney} RUB</b>\n💳 Реквизиты для оплаты: <b>4890 4947 3261 6792</b>\n\nРеквизиты действительны ровно 30 минут, если не успеваете оплатить, пересоздайте сделку, иначе рискуете потерять деньги.\n<b>ВНИМАНИЕ!</b>  Сверяйте номер заказа и реквизиты по которым оплачиваете! Точная сумма, верные реквизиты, иначе рискуете потерять деньги. Если вы оплачиваете через BTC, то автоматическая выдача происходит после 2х подтверждений.", parse_mode='html', reply_markup=markup_reply)	

		# ПОКУПКА МЕФ ЕКБ 2


	if call.data == 'buyekb2':
		zakaz = random.randint(2300, 5000)
		randommoney = random.randint (5710, 5741)
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='❌ Отменить заказ', callback_data='back'))
		bot.send_message(call.message.chat.id, f"<b>Создан заказ #{zakaz}</b>\n\n<b>Екатеринбург | Мефедрон Кристалл 2гр. Тайник</b>\n\n💶 Переведите <b>{randommoney} RUB</b>\n💳 Реквизиты для оплаты: <b>4890 4947 3261 6792</b>\n\nРеквизиты действительны ровно 30 минут, если не успеваете оплатить, пересоздайте сделку, иначе рискуете потерять деньги.\n<b>ВНИМАНИЕ!</b>  Сверяйте номер заказа и реквизиты по которым оплачиваете! Точная сумма, верные реквизиты, иначе рискуете потерять деньги. Если вы оплачиваете через BTC, то автоматическая выдача происходит после 2х подтверждений.", parse_mode='html', reply_markup=markup_reply)	


	if call.data == 'back':
		markup_reply = telebot.types.InlineKeyboardMarkup()
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Тюмень', callback_data=1))
		markup_reply.add(telebot.types.InlineKeyboardButton(text='◽️ Екатеринбург', callback_data=2))
		bot.send_message(call.message.chat.id, '❕❕❕ Вы вернулись в главное меню! Если был создан заказ, то он отменён автоматически ❕❕❕\n\n'
											f'<b>Приветствуем, тебя в Магазине HUGO BOSS SHOP 🙌</b>\n'
											f'В нашем магазине всегда свежие адреса и отличное качество товара. 💎\n'
											f'Перед совершением покупки просим ознакомиться с правилами магазина. 👑\n\n'
											f'<b>/start - меню магазина\n\n</b>'
											f'<b>✅ ВНИМАНИЕ! ОСТЕРЕГАЙТЕСЬ МОШЕННИКОВ! ТОЛЬКО ЭТОТ БОТ ОРИГИНАЛЬНЫЙ!</b>\n'
											f'Мы торгуем только Мефедроном!\n\n'
											f'Будьте уверены в том, что мы тот самый HUGO BOSS SHOP - Свяжитесь с нами по Контактам ниже 👌\n\n'
											f'<b><i>Отзывы на нашем сайте</i></b>\n\n'
											f'<i>Мы будем рады получить обратную связь по качеству продукта/работе магазина/предпочтительным районам</i>\n\n'
											f'<b>Наши контакты:</b>\n'
											f'<b>👇 Клирнет</b>\n'
											f'<b>hugoboss.biz</b>\n'
											f'<b>👇 Onion</b>\n'
											f'<b>3k3wg4ixmguqjlufh6fpwnic6i56hq4jipxwnha675jflj64hnysnaad.onion</b>\n'
											f'<b>👇 OMG Маркетплейс</b>\n'
											f'<b>omgomgomg5j4yrr4mjdv3h5c5xfvxtqqs2in7smi65mjps7wvkmqmtqd.onion/shop/items/57373982-2887-4c25-83cd-6c986c32b6ce</b>\n'
											f'<b>👇 BlackSprut Маркетплейс</b>\n'
											f'<b>blackvcvv4cpsaurawnw7p5yazwfi6djlc77sfgzinexj4ilkmprr2qd.onion/stores/1025</b>\n'
											f'<b>👇Наша ветка на Rutor</b>\n'
											f'<b>http://rutordeepkpafpudl22pbbhzm4llbgncunvgcc66kax55sc4mp4kxcid.onion/threads/hugo-boss-mefedron-opt-i-roznica-ekaterinburg-tjumen.50011</b>', parse_mode='html', reply_markup=markup_reply)






@bot.message_handler(commands=['admin'])
def adminka(message):
	if message.chat.id == admin:
		bot.send_message(message.chat.id, "Введите пароль от админки: ")

	@bot.message_handler(content_types=['text'])
	def getpassword(message):
		getpassword = message.text
		if getpassword == password:
			markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
			stats = types.KeyboardButton("📈 Колличество пользователей")
			rass = types.KeyboardButton("📢 Рассылка сообщений")
			markup_reply.add(stats, rass)
			bot.send_message(message.chat.id, "🤙 Вы в Админке! Воспользуйтесь кнопками ниже.", reply_markup = markup_reply)

		elif message.text == "📈 Колличество пользователей":
			connection = sqlite3.connect("hugoboss.db")
			cursor = connection.cursor()
			cursor.execute("SELECT COUNT(user_id) from USERS	")
			stata_users_ids_message = str(cursor.fetchone()[0])
			bot.send_message(message.chat.id, '📈 Пользователей бота: ' + stata_users_ids_message)
			cursor.close()
			connection.close()

		elif message.text == "📢 Рассылка сообщений":
			msg = bot.send_message(message.from_user.id, "Отправь текст рассылки 👇🏻")
			bot.register_next_step_handler(msg, send_func)

def send_func(message):
	connection = sqlite3.connect("hugoboss.db")
	cursor = connection.cursor()
	cursor.execute("SELECT user_id FROM users")
	results = cursor.fetchall()
	for result in results:
		try:
			message_to_send = message.text
			bot.send_message(result[0], message_to_send)
		except:
			pass
	connection.close()
	bot.send_message(message.from_user.id, "Рассылка успешно завершена ✅")



	




while True:
	try:
		bot.polling(none_stop=True)

	except Exception as e:
		print(e) 
      
		time.sleep(15)
