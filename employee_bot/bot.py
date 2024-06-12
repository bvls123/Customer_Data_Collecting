import telebot

from polls import *

bot = telebot.TeleBot('7191457608:AAHyD8r7S9BIWJRGHwEGzGUC5EdM_fVpMz8')


@bot.message_handler(commands=['start'])
def start(message):
    poll = PersonalData(bot, message)
    poll.start()


@bot.message_handler(commands=['service'])
def service(message):
    poll = ServicePoll(bot, message)
    poll.start()


@bot.message_handler(commands=['monthly_poll'])
def monthly_poll(message):
    if message.chat.id == 686168416:
        response = create_monthly_poll()
        if response.status_code == 200:
            bot.send_message(message.chat.id, 'Опитування створено ✔️')
        else:
            bot.send_message(message.chat.id, '❕Помилка сервера, спробуйте ще раз')
    else:
        bot.send_message(message.chat.id, '❕❕❕Недостатньо прав, тільки адміністратор може створювати опитування')


bot.polling(none_stop=True, interval=0)
