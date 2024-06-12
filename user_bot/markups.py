from telebot import types

def poll_up5():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    markup.add(item1, item2, item3, item4, item5)
    return markup


def poll_up5_skip():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("Пропустити ❌")
    markup.add(item1, item2, item3, item4, item5, item6)
    return markup


def poll_up10():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    item4 = types.KeyboardButton("4")
    item5 = types.KeyboardButton("5")
    item6 = types.KeyboardButton("6")
    item7 = types.KeyboardButton("7")
    item8 = types.KeyboardButton("8")
    item9 = types.KeyboardButton("9")
    item10 = types.KeyboardButton("10")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
    return markup


def poll_accept():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пройти")
    item2 = types.KeyboardButton("Пропустити ❌")
    markup.add(item1, item2)
    return markup


def poll_main():
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("Мої дані 👤", callback_data='personal_data')
    item2 = types.InlineKeyboardButton("Історія послуг 📜", callback_data='services_history')
    item3 = types.InlineKeyboardButton("Про нас ℹ️", callback_data='about_us')
    item4 = types.InlineKeyboardButton("Контакти 📧", callback_data='contacts')
    markup.add(item1, item2, item3, item4)
    return markup

def poll_refund():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Обмін на іншу модель чи пристрій")
    item2 = types.KeyboardButton("Зміна потреби")
    item3 = types.KeyboardButton("Дефекти та пошкодження")
    item4 = types.KeyboardButton("Невідповідність опису")
    item5 = types.KeyboardButton("Неправильна комплектація")
    item6 = types.KeyboardButton("Вирішив обрати інший бренд")
    item7 = types.KeyboardButton("Інше")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    return markup

def poll_social():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Реклама по ТБ")
    item2 = types.KeyboardButton("Реклама в Ютуб")
    item3 = types.KeyboardButton("Реклама в Інстаграм")
    item4 = types.KeyboardButton("Реклама в Фейсбук")
    item5 = types.KeyboardButton("Реклама на вулиці")
    item6 = types.KeyboardButton("Від друзів\знайомих")
    item7 = types.KeyboardButton("Інше")
    markup.add(item1, item2, item3, item4, item5, item6, item7)
    return markup

def skip():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пропустити ❌")
    markup.add(item1)
    return markup

def gender_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Чоловік")
    item2 = types.KeyboardButton("Жінка")
    item3 = types.KeyboardButton("Інше")
    item4 = types.KeyboardButton("Не хочу вказувати")
    markup.add(item1, item2, item3, item4)
    return markup


def regions_markup(regions):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(regions)):
        markup.add(types.KeyboardButton(regions[i]))
    return markup


def cities_markup(cities):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(len(cities)):
        markup.add(types.KeyboardButton(cities[i]))
    return markup