import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime

from loader import dp
from states.register import RegisterState
from utils.db_api.db import UsersFunctionality

users = UsersFunctionality()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f"Salom, {message.from_user.full_name}")
    logging.info(message.date)
    # pretty_txt = (f"<b>Your CHAT ID:</b> {message.chat.id}\n"
    #               f"<em>First Name:</em> {message.chat.first_name}\n"
    #               f"<del>Last Name:</del> {message.chat.last_name}\n"
    #               f"<tg-spoiler>Username:</tg-spoiler> {message.chat.username}\n"
    #               f"<pre>Type: {message.chat.type}</pre>\n"
    #               f"<u>Is Bot: {message.from_user.is_bot}</u>\n"
    #               f"<a href='https://realpython.com'>Language Code: {message.from_user.language_code}</a>\n"
    #               f"<code>Time: {message.date}</code>\n"
    #               f"<blockquote>Message: {message.text}</blockquote>\n"
    #               f"<pre><code class='language-python'>Message type: {message.entities[0].type}</code></pre>\n"
    #               f"Message length: {message.entities[0].length}")

    pretty_txt = ("Botni barcha imkoniyatlaridan to'liq\n"
                  "foydalanish uchun iltimos ro'yxatdan o'ting.\n"
                  "<b>Ismingizni kiriting: </b>\n"
                  "<i>Malasan: <strike>Asadbek Solijonov</strike></i>")

    data_len = len(users.get_all(chat_id=chat_id))

    if data_len == 4:
        await message.answer('Siz ro`yxatda borsiz!')
    else:
        await message.answer(f"{pretty_txt}")
        try:
            users.insert_into(chat_id=message.chat.id)
        except Exception as e:
            logging.warning(f'{e}')
        # Username State start
        await RegisterState.username.set()
