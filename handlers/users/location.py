import logging

from aiogram import types
from loader import dp
from keyboards.default.keyboard import remove_keyboard
from keyboards.inline.keyboard import key


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def location_handler(message: types.Message):
    lo_txt = (f"lat: {message.location.latitude}\n"
              f"lon: {message.location.longitude}")
    await message.answer(f"{lo_txt}", reply_markup=remove_keyboard())
    await message.answer('Do you want to see your id?', reply_markup=key)
