import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime

from loader import dp
from states.register import RegisterState
from utils.db_api.db import UsersFunctionality
from keyboards.inline.keyboard import languages
from handlers.users.translater import Translater

trr = Translater()

users = UsersFunctionality()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    datas = trr.get_data_by_language(chat_id=chat_id)
    await message.answer(f"{datas.get('hello')}, {message.from_user.full_name}")
    logging.info(message.date)
    await message.answer(datas.get('select_language'), reply_markup=languages)


@dp.callback_query_handler(text=['uz', 'ru', 'en'])
async def register_lang(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    users.update_language(chat_id=chat_id, language=call.data)
    datas = trr.get_data_by_language(chat_id=chat_id)
    pretty_txt = datas.get('enter_name')

    data_len = len(users.get_all(chat_id=chat_id))

    if data_len >= 4:
        await call.message.answer(datas.get('already_exists'))
    else:
        await call.message.answer(f"{pretty_txt}")
        try:
            users.insert_into(chat_id=chat_id)
        except Exception as e:
            logging.warning(f'{e}')
        # Username State start
        await RegisterState.username.set()
