from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def contact_keyboard():
    key = ReplyKeyboardMarkup(resize_keyboard=True)
    contact_btn = KeyboardButton('Share Contact', request_contact=True)
    key.add(contact_btn)
    return key


def remove_keyboard():
    return ReplyKeyboardRemove()
