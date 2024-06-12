import telebot
import schedule
import threading
import time

from telebot import types

from markups import poll_main
from polls import *
from services import personal_data_to_text
from api import *


bot = telebot.TeleBot('6054678222:AAEXTqrgByNoQ3keUZ2l2TWGQ6GUa4IuBuw')


def to_main_menu(massage):
    bot.send_message(massage.chat.id, 'Головне меню 🗂️', reply_markup=poll_main())


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, f"👋 Привіт!\n Я бот-асистент, нещодавно ти скористався послугами нашої компанії. \nТобі необхідно ввести певні дані про себе.")
    poll = PersonalData(bot, message)
    poll.start()


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'change':
            poll = PersonalData(bot, call.message)
            poll.start()

        elif call.data == 'main':
            to_main_menu(call.message)

        elif call.data == 'personal_data':
            markup = types.InlineKeyboardMarkup()
            item1 = types.InlineKeyboardButton("Змінити ✏️", callback_data='change')
            item2 = types.InlineKeyboardButton("Головне меню 🗂️", callback_data='main')
            markup.add(item1, item2)
            bot.send_message(call.message.chat.id, personal_data_to_text(get_client_data(call.message.chat.id).json()), reply_markup=markup)

        elif call.data == 'services_history':
            services = get_services_list(call.message.chat.id)
            bot.send_message(call.message.chat.id, f'Історія послуг 📜\n{services_to_text(services)}')
            to_main_menu(call.message)

        elif call.data == 'about_us':
            bot.send_message(call.message.chat.id, 'Ласкаво просимо до нашого Телеграм-бота – вашого надійного помічника! \n Ми створили цей бот спеціально для клієнтів нашої мережі магазинів, щоб забезпечити вам найкращий сервіс і зробити його ще зручнішим та приємнішим.')
            to_main_menu(call.message)

        elif call.data == 'contacts':
            bot.send_message(call.message.chat.id, '☎️ 777-777-77-77 \n✉️777@gmail.com \n🌐@QualityAnalyticUserBot')

            to_main_menu(call.message)


def after_start_poll(telegram_id):
    poll = FirstPoll(bot, telegram_id)
    poll.start()


def monthly_poll(telegram_id):
    poll = MonthlyPoll(bot, telegram_id)
    poll.start()


def shop_poll(telegram_id, service_id):
    poll = ShopPoll(bot, telegram_id, service_id)
    poll.start()


def product_poll(telegram_id, service_id):
    poll = ProductPoll(bot, telegram_id, service_id)
    poll.start()


def refund_poll(telegram_id, service_id):
    poll = RefundPoll(bot, telegram_id, service_id)
    poll.start()


def repair_poll(telegram_id, service_id):
    poll = RepairPoll(bot, telegram_id, service_id)
    poll.start()


def send_get_request():
    response = get('http://127.0.0.1:8000/api/schedule/')
    schedules = response.json()
    if schedules is None:
        return
    for schedule in schedules:

        if len(str(schedule['client'])) > 6:
            print(schedule)
            if schedule['poll_type'] == 'monthly_poll':
                monthly_poll(schedule['client'])
                print(f'monthly_poll sent to {schedule["client"]}')
            elif schedule['poll_type'] == 'first_poll':
                after_start_poll(schedule['client'])
                print(f'first_poll sent to {schedule["client"]}')
            elif schedule['poll_type'] == 'shop_poll':
                shop_poll(schedule['client'], schedule['service'])
                print(f'shop_poll sent to {schedule["client"]}')
            elif schedule['poll_type'] == 'product_poll':
                product_poll(schedule['client'], schedule['service'])
                print(f'product_poll sent to {schedule["client"]}')
            elif schedule['poll_type'] == 'refund_poll':
                refund_poll(schedule['client'], schedule['service'])
                print(f'refund_poll sent to {schedule["client"]}')
            elif schedule['poll_type'] == 'repair_poll':
                repair_poll(schedule['client'], schedule['service'])
                print(f'repair_poll sent to {schedule["client"]}')


def run_scheduler():
    schedule.every(10).seconds.do(send_get_request)
    while True:
        schedule.run_pending()
        time.sleep(1)


thread = threading.Thread(target=run_scheduler)
thread.start()

bot.polling(none_stop=True, interval=0)
