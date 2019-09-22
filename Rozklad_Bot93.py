import telebot as t
from telebot import types
bot = t.TeleBot("839974408:AAHhGvFEiWVnUh3Ujr7LHAvo7JnWxq3zDEE")

@bot.message_handler(commands=["rozklad", "start"])
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', 'Викладачі')
    markup.row("Список групи", "Початок пар")

    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Назад")
def repeat_all_messages(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Розклад', 'Викладачі')
    markup.row("Список групи", "Початок пар")

    bot.send_message(message.chat.id, "Виберіть:", reply_markup = markup)

@bot.message_handler(regexp = "Розклад")
def func(message):
    markup1 = types.ReplyKeyboardMarkup()
    markup1.row('Понеділок', "Вівторок", "Середа")
    markup1.row('Четвер', "П\'ятниця", "Назад")
    bot.send_message(message.chat.id, "Виберіть день тижня:", reply_markup = markup1)


@bot.message_handler(regexp = "Початок пар")
def func(message):
    bot.send_message(message.chat.id, """1 пара 8:30 - 10:05
2 пара 10:25 - 12:00
3 пара 12:20 - 13:55
4 пара 14:15 - 15:50
5 пара 16:10 - 17:45""")

@bot.message_handler(regexp = "Викладачі")
def func1(message):
    bot.send_message(message.chat.id, """1)Долгошей Володимир Борисович (механіка)
2)Єндовицький Павло Олександрович (алгеом)
3)Загородній В'ячеслав Васильович (механіка)
4)Іванова Віта Вікторівна (введ. в спец.)
5)Краков'ян Максим Васильович (прога)
6)Кушлаба Михайло Петрович (укр.)
7)Медкова Ольга Миколаївна (інгліш)
8)Мірошнікова Ірина Юріївна (мат.аналіз)
9)Орєхов Олександр Арсенійович (прога)
10)Пономаренко Сергій Миколайович (введ. в спец.)
11)Хмельницький Микола Олексійович (алгеом)
12)Южакова Ганна Олексіївна (мет.аналіз)
13)Ваш куратор""")

@bot.message_handler(regexp = "Понеділок")
def func2(message):
    bot.send_message(message.chat.id, """1) Математитичний аналіз пр. 155-16
2)Математичний аналіз лекц. 107-7
3)Алгебра та геометрія 154-16
4)English 201-11""")

@bot.message_handler(regexp = "Вівторок")
def func3(message):
    bot.send_message(message.chat.id, """1)[2]Програмування лекц. 215-11
2)Механіка лекц 114-7
3)ФВ
4)[1]Введення в спеціальність лекц. 215-11""")

@bot.message_handler(regexp = "Середа")
def func4(message):
    bot.send_message(message.chat.id, """1)Механіка пр. 155-16
2)[1]Математичний аналіз лекц. 107-7
[2]Україська мова пр. 112-7
3)Алгебра та геометрія лекц. 114-7
4)[1]Алгебра та геометрія лекц. 114-7
[2]Алгебра та геометрія конс. 114-7""")

@bot.message_handler(regexp = "Четвер")
def func5(message):
    bot.send_message(message.chat.id, """1)Механіка л/р 308-4-1
2)Механіка л/р 308-4-1
3)Програмування л/р 308-3-1""")

@bot.message_handler(regexp = "П\'ятниця")
def func6(message):
    bot.send_message(message.chat.id, """1)[1]Введення в спеціальність пр.112-7
[2]Механіка лекц. 112-7
2)[1]Українська мова лекц. 107-7
[2]Введення в спеціальність лекц.205-11""")

@bot.message_handler(regexp = "Список групи")
def func7(message):
    bot.send_message(message.chat.id, """1) Барковський Ярослав Олегович
2) Бездіжий Олег Юрійович
3) Бондар Богдан Сергійович
4) Гавронська Тетяна Сергіївна
5) Горбачов Сергій Олександрович
6) Давиденко Данило Сергійович
7) Девятаєва Анастасія Юріївна
8) Джуган Нікіта Валерійович
9) Дідик Євгенія Анатоліївна
10) Калинник Даніїл Ігорович
11) Карамян Андрій Васильович
12) Куць Андрій Вікторович
13) Ладан Максим Михайлович
14) Лахтуров Микола Васильович
15) Листопад Сергій Віталійович
16) Недождій Олексій Сергійович
17) Перетрухін Сергій Сергійович
18) Прокопивнюк Василь Олександрович
19) Рогальчук Владислав Богданович
20) Сіряк Тетяна Вікторівна
21) Ситник Iлля Олегович""")
if __name__ == '__main__':
    bot.polling(none_stop=True)
