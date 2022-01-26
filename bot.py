import telebot
import requests
import datetime
import pytz
from dateutil.tz import tzutc
from dateutil.relativedelta import *

bot = telebot.TeleBot('1358633577:AAHjEaeUo4Bu39us4ISGOqn3vs1p4MSwTWg')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Расписание на текущую неделю')
keyboard1.row('Cегодня', 'Завтра')
keyboard1.row('Числитель 1', 'Числитель 2')
keyboard1.row('Знаменатель 1', 'Знаменатель 2')

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

rasp_chisl1 = f'''=== Числитель ===

Понедельник:
Отдыхающим привет, работягам с военки соболезную

Вторник:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
6. {para6} Основы информационной безопасности [Пр] | Порсев И.С. | 3226 \n
                 
Среда:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n

Четверг:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Пр] | Антаков М.А. | 4125 \n
2. {para2} Учебно-научный семинар [Пр] | Потапов Д.А. | 4125 \n
3. {para3} Аддитивные технологии в биомедицинской инженерии [Пр] | Рябкин Д.И. | 4125 \n
5. {para5} Безопасность жизнедеятельности [Лек] | Чечерников И.М. | 4305 \n

Пятница:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Лек] | Антаков М.А. | 3303 (м) \n
2. {para2} Аддитивные технологии в биомедицинской инженерии [Лек] | Герасименко А.Ю. | 3102 (м) \n
3. {para3} Основы информационной безопасности [Лек] | Душкин А.В. | 3102 (м) \n
5. {para5} Учебно-научный семинар [Лек] | Потапов Д.А. | 3303 (м) \n

Суббота:
Выходной \n

Воскресенье:
Выходной \n
'''

rasp_chisl2 = f'''=== Числитель ===

Понедельник:
Отдыхающим привет, работягам с военки соболезную \n

Вторник:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
6. {para6} Основы информационной безопасности [Пр] | Порсев И.С. | 3226 \n
                 
Среда:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n

Четверг:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Пр] | Антаков М.А. | 4125 \n
2. {para2} Учебно-научный семинар [Пр] | Потапов Д.А. | 4125 \n
3. {para3} Аддитивные технологии в биомедицинской инженерии [Пр] | Рябкин Д.И. | 4125 \n
5. {para5} Безопасность жизнедеятельности [Лек] | Чечерников И.М. | 4305 \n

Пятница:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Лек] | Антаков М.А. | 3303 (м) \n
2. {para2} Аддитивные технологии в биомедицинской инженерии [Лек] | Герасименко А.Ю. | 3102 (м) \n
3. {para3} Основы информационной безопасности [Лек] | Душкин А.В. | 3102 (м) \n
5. {para5} Учебно-научный семинар [Лек] | Потапов Д.А. | 3303 (м) \n

Суббота:
Выходной \n

Воскресенье:
Выходной \n
'''

rasp_znam1 = f'''=== Знаменатель I ===

Понедельник:
Отдыхающим привет, работягам с военки соболезную \n

Вторник:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
6. {para6} Основы информационной безопасности [Пр] | Порсев И.С. | 3226 \n
                 
Среда:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n

Четверг:
2. {para2} Учебно-научный семинар [Пр] | Потапов Д.А. | 4125 \n
3. {para3} Виртуальные приборы [Лаб] | Литинская Е.Л. | 3112 (м) \n
4. {para4} Виртуальные приборы [Лаб] | Литинская Е.Л. | 3112 (м) \n
5. {para5} Безопасность жизнедеятельности [Лек] | Чечерников И.М. | 4305 \n

Пятница:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Лек] | Антаков М.А. | 3303 (м) \n
2. {para2} Аддитивные технологии в биомедицинской инженерии [Лек] | Герасименко А.Ю. | 3102 (м) \n
3. {para3} Основы информационной безопасности [Лек] | Душкин А.В. | 3102 (м) \n
4. {para4} Безопасность жизнедеятельности [Лаб] | Ковалева Л.Е. | 4207 а \n
5. {para5} Безопасность жизнедеятельности [Лаб] | Ковалева Л.Е. | 4207 а \n

Суббота:
Выходной \n

Воскресенье:
Выходной \n
'''

rasp_znam2 = f'''=== Знаменатель II ===

Понедельник:
Отдыхающим привет, работягам с военки соболезную \n

Вторник:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
6. {para6} Основы информационной безопасности [Пр] | Порсев И.С. | 3226 \n
                 
Среда:
1. {para1} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
2. {para2} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
3. {para3} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
4. {para4} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n
5. {para5} Практика | Преподаватель У.П. | Аудитория практической подготовки БМС 2 \n

Четверг:
2. {para2} Учебно-научный семинар [Пр] | Потапов Д.А. | 4125 \n
3. {para3} Виртуальные приборы [Лаб] | Литинская Е.Л. | 3112 (м) \n
4. {para4} Виртуальные приборы [Лаб] | Литинская Е.Л. | 3112 (м) \n
5. {para5} Безопасность жизнедеятельности [Лек] | Чечерников И.М. | 4305 \n

Пятница:
1. {para1} Контроль качества биомедицинских приборов и программного обеспечения [Лек] | Антаков М.А. | 3303 (м) \n
2. {para2} Аддитивные технологии в биомедицинской инженерии [Лек] | Герасименко А.Ю. | 3102 (м) \n
3. {para3} Основы информационной безопасности [Лек] | Душкин А.В. | 3102 (м) \n

Суббота:
Выходной \n

Воскресенье:
Выходной \n
'''

tzutc = tzutc()
tz = pytz.timezone('Europe/Moscow')


def weekday_count(time):
    start = datetime.datetime(2021, 8, 30, tzinfo=tzutc)
    delta = time - start
    count = delta.days // 7
    return count


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Если что не так, знаешь к кому стучаться', reply_markup=keyboard1)


@bot.message_handler(commands=['send'])
def start_message(message):
    bot.send_message(272451122, 'Хуй', reply_markup=keyboard1)


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


@bot.message_handler(regexp="Числитель 1")
def chisl1_timetable(message):
    bot.send_message(message.chat.id, rasp_chisl1, reply_markup=keyboard1)


@bot.message_handler(regexp="Знаменатель 1")
def znam1_timetable(message):
    bot.send_message(message.chat.id, rasp_znam1, reply_markup=keyboard1)


@bot.message_handler(regexp="Числитель 2")
def chisl2_timetable(message):
    bot.send_message(message.chat.id, rasp_chisl2, reply_markup=keyboard1)


@bot.message_handler(regexp="Знаменатель 2")
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
