import telebot as t
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types
import datetime

#Token = "1266346905:AAFIssbx3Vs92xgJPplzVPuJRu2tQjxJ2z8"


bot = t.TeleBot("1266346905:AAFIssbx3Vs92xgJPplzVPuJRu2tQjxJ2z8")

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
    markup.row('Куратор', "Оголошення")
    markup.row("Корисні посилання", "Повернутися")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Куратор")
def repeat_all_messages(message):
    bot.send_message(message.chat.id, """Кохтич Людмила Михайлівна
+380980241352""")
    
#спимок предподавателей (в предыдущей версии было круче реализованно, писать мне что бы скинул код)
@bot.message_handler(regexp = "Викладачі")
def repeat_all_messages(message):
    bot.send_message(message.chat.id, """Мирошнікова Ірина Юріївна[мат.анал. пр.]
    
    Загородній В\'ячеслав Васильович[мех. лекц.]
    
    Кушлаба Михайло Петрович[укр.м. пр.]
    
    Орєхов Олександр Арсенійович[прог. лекц.]
    
    Чугай Оксана Юріївна[інгліш]
    
    Іванова Віта Вікторівна[введ.в.спец.]
    
    Довгошей Володимир Борисович[мех. пр./лаб.]
    
    Хмельницький Микола Олександрович[алгеом лекц.]
    
    Єндовицький Павло Олександрович[алгеом пр.]
    
    Пономаренко Сергій Миколайович[введ.в.спец.]
    
    Нечипоренко Алла Федорівна[укр.м. лекц.]
    
    Южакова Ганна Олексіївна[мат.анал. лекц.]
    
    Краков\'ян Максимка[прог. лаб.]
    
    Кохтич Людмила Михайлівна[мех. лаб.]""")

@bot.message_handler(regexp = "Корисні посилання")
def repeat_all_messages(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site1= types.InlineKeyboardButton(text='Інформаційний канал', url='https://t.me/Peniamin')
    markup.add(btn_my_site1)
    bot.send_message(message.chat.id, "Посилання:", reply_markup = markup)

@bot.message_handler(regexp = "Оголошення")
def repeat_all_messages(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(5)[0]))


@bot.message_handler(regexp = "Домашнє завдання")
def func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row("Механіка", "Мат.анал.")
    markup.row("Алгеом", "Укр.мова")
    markup.row("Прога", "Введення в спец.")
    markup.row("Англійська")
    markup.row("Назад")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("d")

#Домашка

#в ссылках указание на конкретною ячейку в гугл таблице
@bot.message_handler(regexp = "Механіка")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[0]))

@bot.message_handler(regexp = "Мат.анал.")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Канал', url='https://t.me/nabla_love')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, str(sheet.row_values(2)[1]), reply_markup = markup)

@bot.message_handler(regexp = "Алгеом")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[2]))

@bot.message_handler(regexp = "Укр.мова")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[4]))

@bot.message_handler(regexp = "Прога")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[3]))

@bot.message_handler(regexp = "Введення в спец.")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[5]))

@bot.message_handler(regexp = "Англійська")
def func(message):
    sheet = google()
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, str(sheet.row_values(2)[6]))

    
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
    bot.send_message(message.chat.id, """
1)Іноземна мова
2)Мат.аналіз пр.
3)[1]Мат.аналіз лекц.
4)ФВ""")

@bot.message_handler(regexp = "Вівторок")
def func3(message):
    bot.send_message(message.chat.id, """
1)[2]Програмування лекц.
2)Механіка лекц.
3)Введення в спец.
4)Механіка пр.""")

@bot.message_handler(regexp = "Середа")
def func4(message):
    bot.send_message(message.chat.id, """
1)Алгебра та геометрія лекц. 
2)Алгебра та геометрія пр.
3)
4)[1]Механіка лекц.
[2]Введення в спец.""")

@bot.message_handler(regexp = "Четвер")
def func5(message):
    bot.send_message(message.chat.id, """
1)Алгебра та геометрія лекц.
2)[2] Укр.мова пр.
3)
4)[2] Укр.мова лекц.""")

@bot.message_handler(regexp = "П\'ятниця")
def func6(message):
    bot.send_message(message.chat.id, """
1)Мат.аналіз лекц.
2)Програмування л/р
3)Механіка л/р
4)Механіка л/р""")

#Список группы, что бы узнать вариант в РР
@bot.message_handler(regexp = "Список групи")
def Grupa(message):
    bot.send_message(message.chat.id, """1)Бут Денис Сергійович
2)Ван Їсян
3)Золотко Дмитро Сергійович
4)Зубок Даниіл Миколайович
5)Іванов Віктор Віталійович
6)Карпенко Катерина Максимівна
7)Колесніков Євген Олександрович
8)Корольов Єлисей Володимирович
9)Кравчук Валентин Леонідович
10)Ловцов Станіслав Олегович
11)Локтєва Алла Андріївна
12)Маловичко Роман Ігорович
13)Мітько Євгеній Сергійович
14)Моця Микола Володимирович
15)Назарко Ольга Олександрівна
16)Петренко Дар`я Олександрівна
17)Сівко Вікторія Олексіївна
18)Смоліков Михайло Олексійович
19)Соболєв Андрій Владиславович
20)Черська Анастасія Сергіївна
""")

if __name__ == '__main__':
    bot.polling(none_stop=True)
