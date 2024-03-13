from aiogram import types
from loader import dp


@dp.callback_query_handler(text=["show_id"])
async def show_tg_id(call: types.CallbackQuery):
    await call.message.answer(F"Your id: {call.message.chat.id}")
    # await call.answer(f'Your id: {call.message.chat.id}')
    # await call.answer(cache_time=60)
