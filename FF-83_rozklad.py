import telebot as t
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from telebot import types
import datetime

bot = t.TeleBot("839974408:AAHhGvFEiWVnUh3Ujr7LHAvo7JnWxq3zDEE")

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


@bot.message_handler(regexp = "Домашнє завдання")
def func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row("Дифрівняння")
    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)
    print("d")

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
