from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

key = InlineKeyboardMarkup()
show_id = InlineKeyboardButton(text='show ID', callback_data='show_id')
key.add(show_id)

confirm = InlineKeyboardMarkup()
yes = InlineKeyboardButton(text='Yes', callback_data='yes')
no = InlineKeyboardButton(text='No', callback_data='no')
confirm.add(yes, no)

languages = InlineKeyboardMarkup(row_width=2)
english = InlineKeyboardButton(text='🇺🇸 English', callback_data='en')
russian = InlineKeyboardButton(text='🇷🇺 Russian', callback_data='ru')
uzbek = InlineKeyboardButton(text='🇺🇿 Uzbek', callback_data='uz')
languages.add(english, russian, uzbek)
