from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def contact_location():
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    begin = KeyboardButton('start')
    contact = KeyboardButton('Share Contact', request_contact=True)
    location = KeyboardButton('Share Location', request_location=True)
    key.add(begin, contact, location)
    return key


def remove_keyboard():
    return ReplyKeyboardRemove()
