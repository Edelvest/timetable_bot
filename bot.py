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
keyboard1.row('Расписание на числитель')
keyboard1.row('Расписание на знаменатель')

DAYS = {
	'0': 'Понедельник',
	'1': 'Вторник',
	'2': 'Среда',
	'3': 'Четверг',
	'4': 'Пятница',
	'5': 'Суббота',
	'6': 'Воскресенье',
}

rasp_chisl = '''=== Числитель ===

Понедельник:
2. [10:40-12:10] Физическая культура
3. [12:20/12:50-13:50/14:20] Биомедицинские оптические системы [Пр] (4125)
7. [20:00-21:30] Экономическая теория/Основы рыночной экономики [Онлайн лек.]

Вторник:
1. УВЦ
2. УВЦ
3. УВЦ
4. УВЦ
5. УВЦ
6. УВЦ
7. УВЦ

Среда:
2. [9:00-10:30] Экономическая теория [Пр.] (3129м)
4. [14:30-16:00] Вычислительная томография [Онлайн Пр.]
6. [18:20-19:50] Командная работа и деловые коммуникации [Онлайн лек.]
7. [20:00-21:30] Биомедицинские оптические системы [Онлайн лек.]

Четверг:
1. [9:00-10:30] Биофизические основы живых систем [Пр.] (4125)
2. [10:40-12:10] Физическая культура
7. [20:00-21:30] Прикладная механика [Онлайн лек.]

Пятница:
1. [9:00-10:30] Дискретная математика [Пр.] (3127м)
3. [12:20/12:50-13:50/14:20] Вычислительная томография [Онлайн лек.]
4. [14:30-16:00] Системный анализ [Онлайн лек.]
5. [16:10-17:40] Биофизические основы живых систем [Онлайн лек.]

Суббота:
Выходной

Воскресенье:
Выходной
'''

rasp_znam = '''=== Знаменатель ===

Понедельник:
2. [10:40-12:10] Физическая культура
3. [12:50-14:20] Прикладная механика [Лаб] (4117)
4. [14:30-16:00] Биомедицинские оптические системы [Пр] (4125)

Вторник:
1. УВЦ
2. УВЦ
3. УВЦ
4. УВЦ
5. УВЦ
6. УВЦ
7. УВЦ

Среда:
1. [9:00-10:30] Командная работа и деловые коммуникации [Пр] (3129м)
2. [10:40-12:10] Системный анализ [Пр] (4125)
4. [14:30-16:00] Вычислительная томография [Онлайн Пр.]
6. [18:20-19:50] Командная работа и деловые коммуникации [Онлайн лек.]
7. [20:00-21:30] Биомедицинские оптические системы [Онлайн лек.]

Четверг:
1. [9:00-10:30] Прикладная механика [Пр.] (4218)
2. [10:40-12:10] Физическая культура
6. [18:20-19:50] Дискретная математика [Онлайн лек.]
7. [20:00-21:30] Прикладная механика [Онлайн лек.]

Пятница:
1. [9:00-10:30] Дискретная математика [Пр.] (3127м)
3. [12:20/12:50-13:50/14:20] Вычислительная томография [Онлайн лек.]
4. [14:30-16:00] Системный анализ [Онлайн лек.]
5. [16:10-17:40] Биофизические основы живых систем [Онлайн лек.]

Суббота:
Выходной

Воскресенье:
Выходной
'''

tzutc = tzutc()
tz = pytz.timezone('Europe/Moscow')

def weekday_count(time):
	start = datetime.datetime(2020, 9, 6, tzinfo=tzutc)
	delta = time - start
	count = delta.days // 7
	return count

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Если что не так, знаешь к кому стучаться', reply_markup=keyboard1)


@bot.message_handler(regexp="Расписание на текущую неделю")
def current_week_timetable(message):
	time = datetime.datetime.now(tz)
	if weekday_count(time) % 2 == 0:
		bot.send_message(message.chat.id, rasp_chisl, reply_markup=keyboard1)
	else:
		bot.send_message(message.chat.id, rasp_znam, reply_markup=keyboard1)


@bot.message_handler(regexp="Расписание на числитель")
def chisl_timetable(message):
	bot.send_message(message.chat.id, rasp_chisl, reply_markup=keyboard1)


@bot.message_handler(regexp="Расписание на знаменатель")
def znam_timetable(message):
	bot.send_message(message.chat.id, rasp_znam, reply_markup=keyboard1)


@bot.message_handler(regexp="Cегодня")
def today_timetable(message):
	time = datetime.datetime.now(tz)
	week_num = time.weekday()
	if weekday_count(time) % 2 == 0:
		if week_num != 6:
			today_timetable = rasp_chisl[
				rasp_chisl.find(DAYS[f'{week_num}']):rasp_chisl.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_chisl[rasp_chisl.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
	else:
		if week_num != 6:
			today_timetable = rasp_znam[
				rasp_znam.find(DAYS[f'{week_num}']):rasp_znam.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_znam[rasp_znam.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)


@bot.message_handler(regexp="Завтра")
def next_day_timetable(message):
	time = datetime.datetime.now(tz) + relativedelta(days=+1)
	week_num = time.weekday()
	if weekday_count(time) % 2 == 0:
		if week_num != 6:
			today_timetable = rasp_chisl[
				rasp_chisl.find(DAYS[f'{week_num}']):rasp_chisl.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_chisl[rasp_chisl.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
	else:
		if week_num != 6:
			today_timetable = rasp_znam[
				rasp_znam.find(DAYS[f'{week_num}']):rasp_znam.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_znam[rasp_znam.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
			
bot.polling()