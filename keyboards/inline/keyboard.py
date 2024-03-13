from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key = InlineKeyboardMarkup()
show_id = InlineKeyboardButton(text='show ID', callback_data='show_id')
key.add(show_id)

