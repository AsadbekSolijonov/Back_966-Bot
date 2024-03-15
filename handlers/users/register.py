import logging
import re

from loader import dp
from aiogram import types

from states.register import RegisterState


# Username State handler
@dp.message_handler(content_types=types.ContentTypes.TEXT, state=RegisterState.username)
async def username_register(message: types.Message):
    form = '^[a-z_-]{3,15}$'
    text = message.text
    if re.match(form, text):
        logging.info(f'Username: {message.text}')
        await message.answer(f'Ismingiz <b>{text}</b> qabul qilindi.')
    else:
        await message.answer('Ism xato!\nIltimos qayta <b>ism</b> kiriting')
        return username_register(message)
