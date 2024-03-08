import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime

from keyboards.default.keyboard import contact_location
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")
    logging.info(message.date)
    pretty_txt = (f"<b>Your CHAT ID:</b> {message.chat.id}\n"
                  f"<em>First Name:</em> {message.chat.first_name}\n"
                  f"<del>Last Name:</del> {message.chat.last_name}\n"
                  f"<tg-spoiler>Username:</tg-spoiler> {message.chat.username}\n"
                  f"<pre>Type: {message.chat.type}</pre>\n"
                  f"<u>Is Bot: {message.from_user.is_bot}</u>\n"
                  f"<a href='https://realpython.com'>Language Code: {message.from_user.language_code}</a>\n"
                  f"<code>Time: {message.date}</code>\n"
                  f"<blockquote>Message: {message.text}</blockquote>\n"
                  f"<pre><code class='language-python'>Message type: {message.entities[0].type}</code></pre>\n"
                  f"Message length: {message.entities[0].length}")

    await message.answer(f"{pretty_txt}", reply_markup=contact_location())
