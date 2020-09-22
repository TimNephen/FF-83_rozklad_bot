﻿import telebot as t
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types
import datetime

#Token = "665390764:AAGu-B-QpWmcLsLLY-VS0g3UwVLY0FQyVBA"


bot = t.TeleBot("665390764:AAE9fyGkEw7GJszVzCcuuFkmmTJlHsvFp-c")

#импорт таблицы с гугл диска
def google():
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope )
    client = gspread.authorize(creds)
    return client.open("ДЗшки").sheet1

#первые стартовые кнопки (далее расписаны что каждая кнопка делает)
@bot.message_handler(commands=["rozklad", "start"])
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', "Домашнє завдання")
    markup.row("Номер тижня", "Інше")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Назад")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', "Домашнє завдання")
    markup.row("Номер тижня", "Інше")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("n")

@bot.message_handler(regexp = "Інше")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Викладачі', "Початок пар")
    markup.row("Список групи", "Розрахункова")
    markup.row("Додатково", "Назад")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("i")

@bot.message_handler(regexp = "Повернутися")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Викладачі', "Початок пар")
    markup.row("Список групи", "Номер тижня")
    markup.row("Додатково", "Назад")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("i")

@bot.message_handler(regexp = "Номер тижня")
def repeat_all_messages(message):
    if  (datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day).isocalendar()[1] % 2) == 1:
        bot.send_message(message.chat.id, "Другий тиждень")
    else:
        bot.send_message(message.chat.id, "Перший тиждень")

@bot.message_handler(regexp = "Додатково")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Графік роботи поліклініки', "Оголошення")
    markup.row("Корисні посилання", "Повернутися")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Графік роботи поліклініки")
def repeat_all_messages(message):
    bot.send_message(message.chat.id, """Лікар Ширант Наталія Петрівна
м/с Новікова Наталя Петрівна
Кабінет 3-06
Парні дні  09:00-15:00
Непарні дні 13:00-19:00""")
    
#спимок предподавателей (в предыдущей версии было круче реализованно, писать мне что бы скинул код)
@bot.message_handler(regexp = "Викладачі")
def repeat_all_messages(message):
    bot.send_message(message.chat.id, """Жданов Валерій Іванович
Монастирський Геннадій Євгенович
Кохтич Людмила Михайлівна
Кривенко Ярослав Дмитрович
Оксьоненко Максим Петрович
Доник Тетяна Василівна
Катасонов Антон Анатолійович
Медкова Ольга Миколаївна
Гордійко Наталія Олександрівна
Кузнєцов Микола Юрійович
Кобушкін Олександр Петрович""")

@bot.message_handler(regexp = "Корисні посилання")
def repeat_all_messages(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site1= types.InlineKeyboardButton(text='Інформаційний канал', url='https://t.me/joinchat/AAAAAEt1o7VYZ_tV8S-hLA')
    markup.add(btn_my_site1)
    bot.send_message(message.chat.id, "Посилання:", reply_markup = markup)

@bot.message_handler(regexp = "Оголошення")
def repeat_all_messages(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(4)[0]))


@bot.message_handler(regexp = "Домашнє завдання")
def func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row("Атомна фізика", "Теорія поля")
    markup.row("РМФ", "Теорія ймовірностей")
    markup.row("Обчислювальні методи", "Обробка експерименту")
    markup.row("Англійська", "Коливання та хвилі")
    markup.row("Назад")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("d")

#Домашка

#в ссылках указание на конкретною ячейку в гугл таблице
@bot.message_handler(regexp = "Теорія ймовірностей")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/file/d/121sBO7FjAaF0Vt0lv4I7TYpZDow9dITP/view')
    btn_my_site2= types.InlineKeyboardButton(text='Розв\'язки', url='http://xn--e1avkt.xn--p1ai/%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%A4%D0%B8%D0%BB%D0%B8%D0%BF%D0%BF%D0%BE%D0%B2/')
    markup.add(btn_my_site)
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[3]), reply_markup = markup)

@bot.message_handler(regexp = "Атомна фізика")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Канал', url='https://t.me/atomn20')
    btn_my_site1= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1T05JObPJ_poqpUdmup8pU_if3ex-a_1p')
    markup.add(btn_my_site)
    markup.add(btn_my_site1)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[0]), reply_markup = markup)

@bot.message_handler(regexp = "Теорія поля")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1c_tA8ItpEqD_o6lgcWjJKOCEwWrI1GTW')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[1]), reply_markup = markup)

@bot.message_handler(regexp = "РМФ")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1JfkxsS-IehWufEka_juwIatN365OsUIb')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[2]), reply_markup = markup)

@bot.message_handler(regexp = "Обчислювальні методи")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site2= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1veL5IoEkmcSjFVYIooRPWqhD-zeuYktC')
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[4]), reply_markup = markup)

@bot.message_handler(regexp = "Обробка експерименту")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1nimNZTrmYndV9fajuybi9y7YvTbdVSql')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[5]), reply_markup = markup)

@bot.message_handler(regexp = "Англійська")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1SpWPoqGUATI-t83i6DTJ3GjPOV7Xa80s')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[6]), reply_markup = markup)

@bot.message_handler(regexp = "Коливання та хвилі")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/u/0/folders/1k2c6vZea7-9juMZLvdeI3SRkO90PxKr-')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[7]), reply_markup = markup)



#Домашка


@bot.message_handler(regexp = "Розклад")
def func(message):
    markup1 = types.ReplyKeyboardMarkup()
    markup1.row('Понеділок', "Вівторок", "Середа")
    markup1.row('Четвер', "П\'ятниця", "Назад")
    bot.send_message(message.chat.id, "Виберіть день тижня:", reply_markup = markup1)
    print("r")


@bot.message_handler(regexp = "Початок пар")
def func(message):
    bot.send_message(message.chat.id, """1 пара 8:30 - 10:05
2 пара 10:25 - 12:00
3 пара 12:20 - 13:55
4 пара 14:15 - 15:50
5 пара 16:10 - 17:45""")







# !!! сюда вписывать рассписание своей группы !!!
@bot.message_handler(regexp = "Понеділок")
def func2(message):
    bot.send_message(message.chat.id, """1)Теорія поля лекц. 114-7
2)[1]Теорія поля пр. 114-7""")

@bot.message_handler(regexp = "Вівторок")
def func3(message):
    bot.send_message(message.chat.id, """
1)Коливання та хвилі. лекц. 215-11
2)Атомна фізика. л/р 305-1
3)Атомна фізика. л/р 305-1
4)Атомна фізика. пр. 203-11""")

@bot.message_handler(regexp = "Середа")
def func4(message):
    bot.send_message(message.chat.id, """1)[2]Теорймов пр. 112-7 
2)[2]Обробка експр. лекц.
3)Обробка експр. л/р
4)Коливання та хвилі. пр. 157-1-16""")

@bot.message_handler(regexp = "Четвер")
def func5(message):
    bot.send_message(message.chat.id, """1)[2]РМФ пр.
2)Обчислювальні методи. лекц
3)Іноземна мова
4)Обчислювальні методи. л/р""")

@bot.message_handler(regexp = "П\'ятниця")
def func6(message):
    bot.send_message(message.chat.id, """1)Теор. ймов. лекц.  116-7 
2)РМФ лекц. 215-11
3)Атомна фізика. лекц. 215-11
4)Жданов конс.""")

#Список группы, что бы узнать вариант в РР
@bot.message_handler(regexp = "Список групи")
def Grupa(message):
    bot.send_message(message.chat.id, """1)Грималюк Герман Русланович
2)Єлісєєв Іван Михайлович
3)Жидков Олександр Євгенійович
4)Кобзар Олександр Васильович
5)Коваль Сергій Олександрович
6)Ковальчук Костянтин Віталійович
7)Козловський Артур Андрійович
8)Лантух Софія Юріївна
9)Ланьков Богдан Сергійович
10)Матвєєв Олександр Олексійович
11)Пеньковий Тимофій Олександрович
12)Петрова Тетяна Олександрівна
13)Попівчак Богдан Петрович
14)Сергієнко Анна Романівна
15)Стоян Владислав Віталійович
16)Шокун Артем Дмитрович
17)Шуляк Антон Вікторович""")

if __name__ == '__main__':
    bot.polling(none_stop=True)
