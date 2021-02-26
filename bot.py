import telebot
import requests
import datetime
import pytz
from dateutil.tz import tzutc
from dateutil.relativedelta import *

bot = telebot.TeleBot('1358633577:AAFtPrWHwxmRtUZf0fjGSefAfug1qMbE_Pw')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Расписание на текущую неделю')
keyboard1.row('Cегодня', 'Завтра')
keyboard1.row('Числитель I', 'Числитель II')
keyboard1.row('Знаменатель I', 'Знаментель II')

DAYS = {
    '0': 'Понедельник',
    '1': 'Вторник',
    '2': 'Среда',
    '3': 'Четверг',
    '4': 'Пятница',
    '5': 'Суббота',
    '6': 'Воскресенье',
}
para1 = '[9:00-10:30]'
para2 = '[10:40-12:10]'
para3 = '[12:20/12:50-13:50/14:20]'
para4 = '[14:30-16:00]'
para5 = '[16:10-17:40]'
para6 = '[18:20-19:50]'
para7 = '[20:00-21:30]'
rasp_chisl1 = f'''=== Числитель I===

Понедельник:
1. {para1} Моделирование физиологических процессов [Пр.] (4125)
2. {para2} Физическая культура 
3. {para3} Управление в биотехнических системах [Пр.] (4125)
4. {para4} Оптические методы исследования биосовместимых материалов [Пр.] (4125)
6. {para6} Материаловедение [Онлайн лек.] 
7. {para7} Взаимодействие излучения с рассеивающими средами [Онлайн лек.]

Вторник:
1. УВЦ
2. УВЦ
3. УВЦ
4. УВЦ
5. УВЦ
6. УВЦ
7. УВЦ
                 
Среда:
3. {para3} Методы обработки биомедицинской информации [Лаб.] (3112м) 
4. {para4} Методы обработки биомедицинской информации [Лаб.] (3112м) 
6. {para6} спроводная передача энергии и информации в биологических средах (Онлайн лек.)

Четверг:
1. {para1} Физическая культура
2. {para2} Основы проектирования и конструирования [Лаб.] (4218) 
3. {para3} Основы проектирования и конструирования [Лаб.] (4218) 
5. {para5} Оптические методы исследования биосовместимых материалов (Онлайн лек.)
6. {para6} Основы проектирования и конструирования (Онлайн лек.)
7. {para7} Управление в биотехнических системах (Онлайн лек.)

Пятница:
2. {para2} Взаимодействие излучения с рассеивающими средами (Онлайн пр.)
4. {para4} 3D-моделирование [Пр.] (3105м) 
5. {para5} 3D-моделирование [Пр.] (3105м) 
7. {para7} Моделирование физиологических процессов (Онлайн лекция)

Суббота:
6. {para6} Основы управления проектами (Онлайн лек.)
7. {para7} Методы обработки биомедицинской информации (Онлайн лек.)

Воскресенье:
Выходной
'''

rasp_chisl2 = f'''=== Числитель II ===

Понедельник:
1. {para1} Моделирование физиологических процессов [Пр.] (4125)
2. {para2} Физическая культура 
3. {para3} Управление в биотехнических системах [Пр.] (4125)
4. {para4} Оптические методы исследования биосовместимых материалов [Пр.] (4125)
6. {para6} Материаловедение [Онлайн лек.] 
7. {para7} Взаимодействие излучения с рассеивающими средами [Онлайн лек.]

Вторник:
УВЦ
                 
Среда:
6. {para6} спроводная передача энергии и информации в биологических средах (Онлайн лек.)

Четверг:
1. {para1} Физическая культура
5. {para5} Оптические методы исследования биосовместимых материалов (Онлайн лек.)
6. {para6} Основы проектирования и конструирования (Онлайн лек.)
7. {para7} Управление в биотехнических системах (Онлайн лек.)

Пятница:
2. {para2} Взаимодействие излучения с рассеивающими средами (Онлайн пр.)
4. {para4} 3D-моделирование [Пр.] (3105м) 
5. {para5} 3D-моделирование [Пр.] (3105м) 
7. {para7} Моделирование физиологических процессов (Онлайн лекция)

Суббота:
6. {para6} Основы управления проектами (Онлайн лек.)
7. {para7} Методы обработки биомедицинской информации (Онлайн лек.)

Воскресенье:
Выходной
'''

rasp_znam1 = f'''=== Знаменатель I ===

Понедельник:
1. {para1} Методы обработки биомедицинской информации [Пр.] (4125)
2. {para2} Физическая культура
6. {para6} Материаловедение [Онлайн лек.]
7. {para7} Взаимодействие излучения с рассеивающими средами [Онлайн лек.]

Вторник:
УВЦ

Среда:
6. {para6} Беспроводная передача энергии и информации в биологических средах [Онлайн лек.]

Четверг:
1. {para1} Физическая культура
2. {para2} Материаловедение [Пр.] (4136)
3. {para3} Беспроводная передача энергии и информации в биологических средах [Пр.] (4125)
6. {para6} Основы проектирования и конструирования [Онлайн лек.]
7. {para7} Управление в биотехнических системах [Онлайн лек.]

Пятница:
1. {para1} Основы проектирования и конструирования [Пр.] (4218)
2. {para2} Основы проектирования и конструирования [Пр.] (4218)
3. {para3} Основы управления проектами [Пр.] (4326а)
7. {para7} Моделирование физиологических процессов [Онлайн лек.]

Суббота:
6. {para6} Основы управления проектами [Лек]
7. {para7} Методы обработки биомедицинской информации [Лек] 

Воскресенье:
Выходной
'''

rasp_znam2 = f'''=== Знаменатель II ===

Понедельник:
1. {para1} Методы обработки биомедицинской информации [Пр.] (4125)
2. {para2} Физическая культура
6. {para6} Материаловедение [Онлайн лек.]
7. {para7} Взаимодействие излучения с рассеивающими средами [Онлайн лек.]

Вторник:
УВЦ

Среда:
6. {para6} Беспроводная передача энергии и информации в биологических средах [Онлайн лек.]
7. {para7} Оптические методы исследования биосовместимых материалов [Онлайн лек.] (4204м)

Четверг:
1. {para1} Физическая культура
2. {para2} Материаловедение [Пр.] (4136)
3. {para3} Беспроводная передача энергии и информации в биологических средах [Пр.] (4125)
6. {para6} Основы проектирования и конструирования [Онлайн лек.]
7. {para7} Управление в биотехнических системах [Онлайн лек.]

Пятница:
3. {para3} Основы управления проектами [Пр.] (4326а)
4. {para4} 3D-моделирование [Пр.] (3105м) 
5. {para5} 3D-моделирование [Пр.] (3105м) 
7. {para7} Моделирование физиологических процессов [Онлайн лек.]

Суббота:
6. {para6} Основы управления проектами [Лек]
7. {para7} Методы обработки биомедицинской информации [Лек] 

Воскресенье:
Выходной
'''

tzutc = tzutc()
tz = pytz.timezone('Europe/Moscow')


def weekday_count(time):
    start = datetime.datetime(2021, 2, 7, tzinfo=tzutc)
    delta = time - start
    count = delta.days // 7
    return count


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Если что не так, знаешь к кому стучаться', reply_markup=keyboard1)


@bot.message_handler(regexp="Расписание на текущую неделю")
def current_week_timetable(message):
    time = datetime.datetime.now(tz)
    if weekday_count(time) % 4 == 0:
        bot.send_message(message.chat.id, rasp_chisl1, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 1:
        bot.send_message(message.chat.id, rasp_znam1, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 2:
        bot.send_message(message.chat.id, rasp_chisl2, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 3:
        bot.send_message(message.chat.id, rasp_znam2, reply_markup=keyboard1)


@bot.message_handler(regexp="Числитель I")
def chisl1_timetable(message):
    bot.send_message(message.chat.id, rasp_chisl1, reply_markup=keyboard1)


@bot.message_handler(regexp="Числитель II")
def chisl2_timetable(message):
    bot.send_message(message.chat.id, rasp_chisl2, reply_markup=keyboard1)


@bot.message_handler(regexp="Знаменатель I")
def znam1_timetable(message):
    bot.send_message(message.chat.id, rasp_znam1, reply_markup=keyboard1)


@bot.message_handler(regexp="Знаменатель II")
def znam2_timetable(message):
    bot.send_message(message.chat.id, rasp_znam2, reply_markup=keyboard1)


@bot.message_handler(regexp="Cегодня")
def today_timetable(message):
    time = datetime.datetime.now(tz)
    week_num = time.weekday()
    if weekday_count(time) % 4 == 0:
        if week_num != 6:
            today_timetable = rasp_chisl1[
                              rasp_chisl1.find(DAYS[f'{week_num}']):rasp_chisl1.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_chisl1[rasp_chisl1.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 1:
        if week_num != 6:
            today_timetable = rasp_znam1[
                              rasp_znam1.find(DAYS[f'{week_num}']):rasp_znam1.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_znam1[rasp_znam1.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 2:
        if week_num != 6:
            today_timetable = rasp_chisl2[
                              rasp_chisl2.find(DAYS[f'{week_num}']):rasp_chisl2.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_chisl2[rasp_chisl2.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 3:
        if week_num != 6:
            today_timetable = rasp_znam2[
                              rasp_znam2.find(DAYS[f'{week_num}']):rasp_znam2.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_znam2[rasp_znam2.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)


@bot.message_handler(regexp="Завтра")
def next_day_timetable(message):
    time = datetime.datetime.now(tz) + relativedelta(days=+1)
    week_num = time.weekday()
    if weekday_count(time) % 4 == 0:
        if week_num != 6:
            today_timetable = rasp_chisl1[
                              rasp_chisl1.find(DAYS[f'{week_num}']):rasp_chisl1.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_chisl1[rasp_chisl1.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 1:
        if week_num != 6:
            today_timetable = rasp_znam1[
                              rasp_znam1.find(DAYS[f'{week_num}']):rasp_znam1.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_znam1[rasp_znam1.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 2:
        if week_num != 6:
            today_timetable = rasp_chisl2[
                              rasp_chisl2.find(DAYS[f'{week_num}']):rasp_chisl2.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_chisl2[rasp_chisl2.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
    elif weekday_count(time) % 4 == 3:
        if week_num != 6:
            today_timetable = rasp_znam2[
                              rasp_znam2.find(DAYS[f'{week_num}']):rasp_znam2.find(DAYS[f'{week_num + 1}'])
                              ]
        else:
            today_timetable = rasp_znam2[rasp_znam2.find(DAYS[f'{week_num}'])::]
        bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)


bot.polling()
