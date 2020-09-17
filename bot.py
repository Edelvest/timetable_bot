import telebot
import requests
import datetime
import pytz
from dateutil.tz import tzutc

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
}

rasp_chisl = '''=== Числитель ===

Понедельник:
2. Физическая культура
3. Биомедицинские оптические системы [Пр] (4125)
7. Экономическая теория/Основы рыночной экономики [Онлайн лек.]

Вторник:
1. УВЦ
2. УВЦ
3. УВЦ
4. УВЦ
5. УВЦ
6. УВЦ
7. УВЦ

Среда:
1. Экономическая теория [Пр.] (3129м)
4. Вычислительная томография [Онлайн Пр.]
6. Командная работа и деловые коммуникации [Онлайн лек.]
7. Биомедицинские оптические системы [Онлайн лек.]

Четверг:
1. Биофизические основы живых систем [Пр.] (4125)
2. Физическая культура
7. Прикладная механика [Онлайн лек.]

Пятница:
1. Дискретная математика [Пр.] (3127м)
3. Вычислительная томография [Онлайн лек.]
4. Системный анализ [Онлайн лек.]
5. Биофизические основы живых систем [Онлайн лек.]

'''

rasp_znam = '''=== Знаменатель ===

Понедельник:
2. Физическая культура
3. Прикладная механика [Лаб] (4117)
4. Биомедицинские оптические системы [Пр] (4125)

Вторник:
1. УВЦ
2. УВЦ
3. УВЦ
4. УВЦ
5. УВЦ
6. УВЦ
7. УВЦ

Среда:
1. Командная работа и деловые коммуникации [Пр] (3129м)
2. Системный анализ [Пр] (4125)
4. Вычислительная томография [Онлайн Пр.]
6. Командная работа и деловые коммуникации [Онлайн лек.]
7. Биомедицинские оптические системы [Онлайн лек.]

Четверг:
1. Прикладная механика [Пр.] (4218)
2. Физическая культура
6. Дискретная математика [Онлайн лек.]
7. Прикладная механика [Онлайн лек.]

Пятница:
1. Дискретная математика [Пр.] (3127м)
3. Вычислительная томография [Онлайн лек.]
4. Системный анализ [Онлайн лек.]
5. Биофизические основы живых систем [Онлайн лек.]
'''

tzutc = tzutc()
tz = pytz.timezone('Europe/Moscow')
time = datetime.datetime.now(tz)
start = datetime.datetime(2020, 9, 7, tzinfo=tzutc)

def weekday_count():
	delta = time - start
	count = delta.days // 7
	return count

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Если что не так, знаешь к кому стучаться', reply_markup=keyboard1)


@bot.message_handler(regexp="Расписание на текущую неделю")
def current_week_timetable(message):
	if weekday_count() % 2 == 0:
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
	week_num = time.weekday()
	if weekday_count() % 2 == 0:
		if week_num != 4:
			today_timetable = rasp_chisl[
				rasp_chisl.find(DAYS[f'{week_num}']):rasp_chisl.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_chisl[rasp_chisl.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
	else:
		if week_num != 4:
			today_timetable = rasp_znam[
				rasp_znam.find(DAYS[f'{week_num}']):rasp_znam.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_znam[rasp_znam.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)


@bot.message_handler(regexp="Завтра")
def next_day_timetable(message):
	week_num = time.weekday() + 1
	if weekday_count() % 2 == 0:
		if week_num != 4:
			today_timetable = rasp_chisl[
				rasp_chisl.find(DAYS[f'{week_num}']):rasp_chisl.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_chisl[rasp_chisl.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
	else:
		if week_num != 4:
			today_timetable = rasp_znam[
				rasp_znam.find(DAYS[f'{week_num}']):rasp_znam.find(DAYS[f'{week_num+1}'])
			]
		else:
			today_timetable = rasp_znam[rasp_znam.find(DAYS[f'{week_num}'])::]
		bot.send_message(message.chat.id, today_timetable, reply_markup=keyboard1)
			
bot.polling()