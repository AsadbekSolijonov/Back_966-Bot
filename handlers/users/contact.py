import logging

from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_handler(message: types.Message):
    await message.answer(f"{message.contact.phone_number}")
