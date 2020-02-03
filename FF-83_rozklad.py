import telebot as t
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types
import datetime

#Token = "665390764:AAGu-B-QpWmcLsLLY-VS0g3UwVLY0FQyVBA"


bot = t.TeleBot("665390764:AAGu-B-QpWmcLsLLY-VS0g3UwVLY0FQyVBA")

def google():
    scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope )
    client = gspread.authorize(creds)
    return client.open("Домашка").sheet1

@bot.message_handler(commands=["rozklad", "start"])
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', "Домашнє завдання")
    markup.row("Розрахункова", "Інше")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Назад")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', "Домашнє завдання")
    markup.row("Розрахункова", "Інше")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("n")

@bot.message_handler(regexp = "Інше")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Викладачі', "Початок пар")
    markup.row("Список групи", "Номер тижня")
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
    bot.send_message(message.chat.id, str(sheet.row_values(2)[7]))


@bot.message_handler(regexp = "Домашнє завдання")
def func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row("Дифрівняння")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("d")

#Домашка

@bot.message_handler(regexp = "Дифрівняння")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/file/d/121sBO7FjAaF0Vt0lv4I7TYpZDow9dITP/view')
    btn_my_site2= types.InlineKeyboardButton(text='Розв\'язки', url='http://xn--e1avkt.xn--p1ai/%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%A4%D0%B8%D0%BB%D0%B8%D0%BF%D0%BF%D0%BE%D0%B2/')
    markup.add(btn_my_site)
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[3]), reply_markup = markup)

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





@bot.message_handler(regexp = "Викладачі")
def prepody(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site1= types.InlineKeyboardButton(text='Гільчук А.В.', callback_data="G")
    btn_my_site= types.InlineKeyboardButton(text='Кравцов О.В.', callback_data="Kr")
    btn_my_site2= types.InlineKeyboardButton(text='Наказной П.О.', callback_data="Na")
    btn_my_site3= types.InlineKeyboardButton(text='Парновський С.Л.', callback_data="Pa")
    btn_my_site4= types.InlineKeyboardButton(text='Пономаренко С.М.', callback_data="Po")
    btn_my_site5= types.InlineKeyboardButton(text='Рибак О.В.', callback_data="Ry")
    btn_my_site6= types.InlineKeyboardButton(text='Рябов Г.В.', callback_data="Ra")
    btn_my_site7= types.InlineKeyboardButton(text='Чугай О.Ю.', callback_data="C")
    btn_my_site8= types.InlineKeyboardButton(text='Мулярчук М.А.', callback_data="M")
    markup.add(btn_my_site1, btn_my_site)
    markup.add(btn_my_site8, btn_my_site2)
    markup.add(btn_my_site3, btn_my_site4)
    markup.add(btn_my_site5, btn_my_site6)
    markup.add(btn_my_site7)
    bot.send_message(message.chat.id, "Виберіть викладача: " , reply_markup = markup)

@bot.callback_query_handler(func=lambda call: True)
def prepody(call):
    if call.data == "G":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoG")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Гільчук Андрій Володимирович
Викладає: Термодинаміка газового потоку/лекція""", reply_markup = markup)
    elif call.data == "Kr":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoKr")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Кравцов Олег Васильович
Викладає: Класична механіка/лекція""", reply_markup = markup)
    elif call.data == "M":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoM")
        markup.add(btn_my_site1)
        markup.add(btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Мулярчук Марія Андріївна
Викладає: Термодинаміка газового потоку/практика""", reply_markup = markup)
    elif call.data == "Na":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoNa")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Наказной Павло Олександрович
Викладає: Диференціальні рівняння/практика
Класична механіка/практика
Тензорний аналіз/лекція""", reply_markup = markup)
    elif call.data == "Pa":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoPa")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Парновський Сергій Людомирович
Викладає: Електрика та магнетизм/лекція""", reply_markup = markup)
    elif call.data == "Po":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoPo")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Пономаренко Сергій Миколайович
Викладає: Електрика та магнетизм/практика""", reply_markup = markup)
    elif call.data == "Ry":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoRy")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Рибак Олександр Владиславович
Викладає: Математичний аналіз/лекція""", reply_markup = markup)
    elif call.data == "Ra":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoRa")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Рябов Георгій Валентинович
Викладає: Диференціальні рівняння/лекція""", reply_markup = markup)
    elif call.data == "C":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Назад', callback_data="back")
        btn_my_site2= types.InlineKeyboardButton(text='Фото', callback_data="photoC")
        markup.add(btn_my_site1, btn_my_site2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Чугай Оксана Юріївна
Викладає: Англійська мова/практика""", reply_markup = markup)

    elif call.data == "photoG":
            f = open("Гільчук.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoKr":
            f = open("Кравцов.png"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoM":
            f = open("Мулярчук.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoNa":
            f = open("Наказной.png"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoPa":
                f = open("Парновський.jpg"   , 'rb')
                bot.send_photo(call.message.chat.id, f)
                f.close()
    elif call.data == "photoPo":
            f = open("Пономаренко.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoRy":
            f = open("Рибак.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoRa":
            f = open("Рябов.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()
    elif call.data == "photoC":
            f = open("Чугай.jpg"   , 'rb')
            bot.send_photo(call.message.chat.id, f)
            f.close()

    elif call.data == "back":

        markup = types.InlineKeyboardMarkup()
        btn_my_site1= types.InlineKeyboardButton(text='Гільчук А.В.', callback_data="G")
        btn_my_site= types.InlineKeyboardButton(text='Кравцов О.В.', callback_data="Kr")
        btn_my_site2= types.InlineKeyboardButton(text='Наказной П.О.', callback_data="Na")
        btn_my_site3= types.InlineKeyboardButton(text='Парновський С.Л.', callback_data="Pa")
        btn_my_site4= types.InlineKeyboardButton(text='Пономаренко С.М.', callback_data="Po")
        btn_my_site5= types.InlineKeyboardButton(text='Рибак О.В.', callback_data="Ry")
        btn_my_site6= types.InlineKeyboardButton(text='Рябов Г.В.', callback_data="Ra")
        btn_my_site7= types.InlineKeyboardButton(text='Чугай О.Ю.', callback_data="C")
        btn_my_site8= types.InlineKeyboardButton(text='Мулярчук М.А.', callback_data="M")
        markup.add(btn_my_site1, btn_my_site)
        markup.add(btn_my_site8, btn_my_site2)
        markup.add(btn_my_site3, btn_my_site4)
        markup.add(btn_my_site5, btn_my_site6)
        markup.add(btn_my_site7)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id= call.message.message_id, text = "Виберіть викладача", reply_markup = markup)


@bot.message_handler(regexp = "Розрахункова")
def func(message):
    markup1 = types.ReplyKeyboardMarkup()
    markup1.row("Повний")
    markup1.row("Чіііілллл")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup1)

@bot.message_handler(regexp = "Понеділок")
def func2(message):
    bot.send_message(message.chat.id, """2)Оптика пр. 205-11
3)[1]Філософія пр. 144-16
[2]Психологія пр. 153-16
4)ФВ""")

@bot.message_handler(regexp = "Вівторок")
def func3(message):
    bot.send_message(message.chat.id, """1)[2] ВДЕ пр. 201-11
2)ВДЕ лекц. 201-11
3)Основи теплоенергетики лекц. 201-11
4)[1] Основи теплоенергетики пр. 201-11
[2]Психологія лекц. 112-7""")

@bot.message_handler(regexp = "Середа")
def func4(message):
    bot.send_message(message.chat.id, """1)ТФКЗ лекц. 112-7
2)[1] Дифрівняння лекц. 107-7
3)Класична механіка 114-7
4)Оптика л/р 308-4-1
5)Оптика л/р 308-4-1""")

@bot.message_handler(regexp = "Четвер")
def func5(message):
    bot.send_message(message.chat.id, """1)[2] Філософія лекц. 107-7
2)ТФКЗ пр. 142-16
3)Класична механіка  пр. 142-16""")

@bot.message_handler(regexp = "П\'ятниця")
def func6(message):
    bot.send_message(message.chat.id, """1)English 204-11
2)Оптика лекц. 215-11
3)[2]Дифрівняння пр. 142-16""")

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
11)Павлюченко Дмитро Андрійович
12)Пеньковий Тимофій Олександрович
13)Петрова Тетяна Олександрівна
14)Попівчак Богдан Петрович
15)Сергієнко Анна Романівна
16)Стоян Владислав Віталійович  
17)Шокун Артем Дмитрович
18)Шуляк Антон Вікторович""")

if __name__ == '__main__':
    bot.polling(none_stop=True)
