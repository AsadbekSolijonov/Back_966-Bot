from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key = InlineKeyboardMarkup()
show_id = InlineKeyboardButton(text='show ID', callback_data='show_id')
key.add(show_id)


confirm = InlineKeyboardMarkup()
yes = InlineKeyboardButton(text='Yes', callback_data='yes')
no = InlineKeyboardButton(text='No', callback_data='no')
confirm.add(yes, no)

