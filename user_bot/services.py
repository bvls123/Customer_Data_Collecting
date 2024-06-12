import re

from datetime import datetime
from dateutil import parser

from api import *


def personal_data_to_text(data):
    text = f"Ім'я: {data['first_name']}\n" \
           f"Прізвище: {data['last_name']}\n" \
           f"Стать: {data['gender']}\n" \
           f"Вік: {data['age']}\n" \
           f"Електронна пошта ✉️: {data['email']}\n" \
           f"Телефон 📱: {data['phone']}\n" \
           f"Район 🏙️: {get_city_name(data['city'])}\n"
    return text


def is_mail_correct(mail):
    return re.match(r"[^@]+@[^@]+\.[^@]+", mail) is not None


def is_phone_correct(phone):
    return phone.isdigit() and len(phone) == 10


def cities_to_text(cities):
    text = ''
    for i in range(len(cities)):
        text += f"{i + 1}. {cities[i]}\n"
    return text


#{'id': 1, 'serviceType': 'Покупка', 'payment': 'івадло', 'warranty': False, 'datetime': '2024-05-24T13:10:17.340120Z', 'employee': 1, 'client': 1, 'nomenclature': 1}
def services_to_text(services):
    text = '\n'
    if len(services) == 0:
        return 'Немає послуг'
    for i in range(len(services)):
        print(services[i])
        print(get_nomenclature(services[i]['nomenclature']))
        datetime = parser.parse(services[i]['datetime'])
        datetime = f"{datetime.year}-{datetime.month}-{datetime.day}"
        nomenclature = get_nomenclature(services[i]['nomenclature'])['name']
        if services[i]['serviceType'] == 'Покупка' or services[i]['serviceType'] == 'Покупка(франшиза)':
            text += (f"{i + 1}. {services[i]['serviceType']} "
                     f"\nДата 🗓️: {datetime} "
                     f"\nОдиниця 🛠️: {nomenclature} "
                     f"\nОплата: {services[i]['payment']} \n\n")
        if services[i]['serviceType'] == 'Ремонт':
            text += (f"{i + 1}. {services[i]['serviceType']} "
                     f"\nДата 🗓️: {datetime} "
                     f"\nОдиниця 🛠️: {nomenclature} "
                     f"\nГарантія: {'Так' if services[i]['warranty'] else 'Ні'} \n\n")
        if services[i]['serviceType'] == 'Повернення':
            text += (f"{i + 1}. {services[i]['serviceType']} "
                     f"\nДата 🗓️: {datetime} "
                     f"\nОдиниця 🛠️: {nomenclature} \n\n")
    return text
