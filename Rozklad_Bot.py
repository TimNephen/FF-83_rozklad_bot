import telebot as t
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
    return client.open("Домашка").sheet1

#первые стартовые кнопки (далее расписаны что каждая кнопка делает)
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
    
#спимок предподавателей (в предыдущей версии было круче реализованно, писать мне что бы скинул код)
@bot.message_handler(regexp = "Викладачі")
def repeat_all_messages(message):
    bot.send_message(message.chat.id, """Іванова Віта Вікторівна
Бабіна Світлана Іванівна
Москаленко Ольга Володимирівна
Панченко Надія Анатоліївна
Борисенко Андрій Володимирович
Пешко Віталій Анатолійович
Ложкін Георгій Володимирович
Наказной Павло Олександрович
Рябов Георгій Валентинович
Кравцов Олег Васильович
Пономаренко Сергій Миколайович
Зарівна Оксана Тимофіївна
Парновський Сергій Людомирович""")

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
    markup.row("Оптика", "ВДЕ")
    markup.row("Енергетика", "ТФКП")
    markup.row("Дифрівняння", "Класична механіка")
    markup.row("Англійська", "Філософія")
    markup.row("Психологія", "Назад")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("d")

#Домашка

#в ссылках указание на конкретною ячейку в гугл таблице
@bot.message_handler(regexp = "Дифрівняння")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/file/d/121sBO7FjAaF0Vt0lv4I7TYpZDow9dITP/view')
    btn_my_site2= types.InlineKeyboardButton(text='Розв\'язки', url='http://xn--e1avkt.xn--p1ai/%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0/%D0%A4%D0%B8%D0%BB%D0%B8%D0%BF%D0%BF%D0%BE%D0%B2/')
    markup.add(btn_my_site)
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[3]), reply_markup = markup)

@bot.message_handler(regexp = "Оптика")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/open?id=1jMt5l3Tne1TvhYnumcBAnW0Cd9BMGIpy')
    btn_my_site2= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1jKtV-7m_X871YQW5QOKCFPb47JHMKMuj')
    markup.add(btn_my_site)
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[0]), reply_markup = markup)

@bot.message_handler(regexp = "ВДЕ")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1rEidHOMQnPUApMDrHu91bBE4NdguW9W7')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[1]), reply_markup = markup)

@bot.message_handler(regexp = "Енергетика")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1M5TIE1wFx7VBJJhgyRFQAgulyZbHz6O6')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[2]), reply_markup = markup)

@bot.message_handler(regexp = "ТФКП")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/open?id=1kXCm5OcduKnXSK7o8PJHAcS4Lg75Epa2')
    btn_my_site2= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1eAnYMn1E2QillBFZUJFCqIU2r8MNOvr-')
    markup.add(btn_my_site)
    markup.add(btn_my_site2)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[4]), reply_markup = markup)

@bot.message_handler(regexp = "Класична механіка")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Задачник', url='https://drive.google.com/open?id=1gKsBEEwqgysOFu6V5Y9nI-iu0gLKrpYl')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[5]), reply_markup = markup)

@bot.message_handler(regexp = "Англійська")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Підручник', url='https://drive.google.com/open?id=0B1GYLTRP36rtQzJ0RWw2ZVFoM0h3Q1QtVG5ER05Qd1RWamVB')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[6]), reply_markup = markup)

@bot.message_handler(regexp = "Філософія")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1thipJINDPoDmxqKC3Dq_Pi96doEixr9i')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[7]), reply_markup = markup)

@bot.message_handler(regexp = "Психологія")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Розділ на диску', url='https://drive.google.com/drive/folders/1zZ11wfah-YLZlu1O5fE4rKRLE3U9bJwh')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[8]), reply_markup = markup)

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
    bot.send_message(message.chat.id, """1)Теплоенергетика лекц. 201-11
2)Оптика пр. 205-11
3)[1]Філософія пр. 144-16
[2]Психологія пр. 153-16
4)ФВ""")

@bot.message_handler(regexp = "Вівторок")
def func3(message):
    bot.send_message(message.chat.id, """
2)ВДЕ лекц. 201-11
3)[2]ВДЕ пр. 201-11
4)[2]Психологія лекц. 112-7""")

@bot.message_handler(regexp = "Середа")
def func4(message):
    bot.send_message(message.chat.id, """1)ТФКЗ лекц. 112-7
2)[1]Дифрівняння лекц. 107-7
[2]Теплоенергетика пр. 142-16
3)Класична механіка лекц. 114-7
4)Оптика л/р 308-4-1
5)Оптика л/р 308-4-1""")

@bot.message_handler(regexp = "Четвер")
def func5(message):
    bot.send_message(message.chat.id, """1)[2]Філософія лекц. 107-7
2)ТФКЗ пр. 142-16
3)Класична механіка  пр. 142-16""")

@bot.message_handler(regexp = "П\'ятниця")
def func6(message):
    bot.send_message(message.chat.id, """1)English 143-16
2)Оптика лекц. 215-11
3)[2]Дифрівняння пр. 201-11""")

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
