from calendar import weekheader
from parsing import pogoda

import telebot
import datetime

keybord1=telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет','Пока')
keybord1.row('Дата','время','День недели')
bot=telebot.TeleBot('************************************************')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет, ты написал мне /start',reply_markup=keybord1)




@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message)
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id,'И тебе привет!')
    elif message.text.lower()=='пока':
        bot.send_message(message.chat.id,'и тебе пока!')
    elif message.text.lower()=='дата':
        data=datetime.date.today()
        bot.send_message(message.chat.id,data)
    elif message.text.lower()=='время':
        time=datetime.datetime.today().strftime("%H:%M:%S")
        bot.send_message(message.chat.id,time)
    elif message.text.lower()=='день недели':
        weekday=datetime.datetime.today().strftime("%A")
        bot.send_message(message.chat.id,weekday)
    elif message.text.lower().startswith('день рождения'):
        num=message.text[13:].split()
        try:
            day=int(num[0])
            mounth=int(num[1])
            year=int(num[2])
            data1=datetime.date(year,mounth,day)
            today=datetime.date.today()
            data=today-data1
            bot.send_message(message.chat.id,f'Со дня вашего рождения прошло {data.days} дней')
        except:
            bot.send_message(message.chat.id,'Произошла ошибка! напишите по премеру ')
            bot.send_message(message.chat.id,'премер: день рождения (день) (месяц) (год)')
    elif message.text.lower()=='справка':
        bot.send_message(message.chat.id, 'Справка: день рождения (день) (месяц) (год) :Выводит сколько дней вы прожили')
        bot.send_message(message.chat.id,
                         'tg:Выводит мой tg канал')
        bot.send_message(message.chat.id,
                         'разработчик:выводит данные разработчика')
    elif message.text.lower()=='tg':
        bot.send_message(message.chat.id,'https://t.me/vadik_gad1k')
    elif message.text.lower()=='разработчик':
        bot.send_message(message.chat.id,'Привет меня зовут Вадим')
        bot.send_message(message.chat.id,'я програмирую уже 1 год')
        bot.send_message(message.chat.id,'если хотите узнать о мне больше переходите в мой тг (напишите tg)')
    elif message.text.lower()=='погода':
        result=pogoda()
        bot.send_message(message.chat.id,result[0])
        bot.send_message(message.chat.id, result[1])
bot.polling()