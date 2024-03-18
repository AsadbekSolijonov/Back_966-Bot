import logging
import re

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import state

from keyboards.default.keyboard import contact_keyboard
from loader import dp
from aiogram import types

from states.register import RegisterState


# Username Handler State
@dp.message_handler(content_types=types.ContentTypes.TEXT, state=RegisterState.username)
async def username_register(message: types.Message, state: FSMContext):
    form = '^[a-z_-]{3,15}$'
    text = message.text.lower()
    if re.match(form, text):
        logging.info(f'Username: {message.text}')
        await message.answer(f'Ismingiz <b>{text.title()}</b> qabul qilindi.')
        # FSMContext ga saqlab olish
        async with state.proxy() as storage:
            storage['username'] = text.title()

        # Keyingi bosqichga o'tish
        await RegisterState.phone.set()
        await message.answer('Iltimos telefon raqamingizni yuboring:', reply_markup=contact_keyboard())
    else:
        await message.answer('Ism xato!\nIltimos qayta <b>ism</b> kiriting')
        return username_register(message)


# Handler Phone State
@dp.message_handler(content_types=types.ContentTypes.CONTACT, state=RegisterState.phone)
async def phone_register(message: types.Message, state: FSMContext):
    contact = message.contact.phone_number
    await message.answer(f"<b>{contact}</b> qabul qilindi!")
    # FSMContext ga saqlab olish
    async with state.proxy() as storage:
        storage['phone'] = contact
    # Keyingi bosqichga o'tish
    await RegisterState.address.set()
    await message.answer(f'Iltimos addressingizni to`liq kiriting:')


# Handler Address State
@dp.message_handler(content_types=types.ContentTypes.TEXT, state=RegisterState.address)
async def address_register(message: types.Message, state: FSMContext):
    address = message.text.title()
    await message.answer(f"<b>{address}</b> qabul qilindi!")
    # FSMContext dan oq'ish
    async with state.proxy() as storage:
        username = storage['username']
        phone = storage['phone']
    # datas saved to database

    await state.finish()
