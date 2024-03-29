from aiogram import types
from loader import dp
from utils.db_api.db import UsersFunctionality
from keyboards.inline.keyboard import confirm

users = UsersFunctionality()
CHAT_IDS = None


@dp.message_handler(commands=['obunachilar'])
async def subscribe(message: types.Message):
    followers = users.get_followers_count()
    await message.answer(f'Obunachilar soni {followers} ta.')


@dp.message_handler(commands=['followers'])
async def get_followers(message: types.Message):
    text = ""
    for follow in users.get_followers():
        text += f"{follow[0]}. {follow[1]}\n"
    await message.answer(text)


@dp.message_handler(lambda message: message.text.startswith('/del'))
async def del_user(message: types.Message):
    global CHAT_IDS
    chat_ids = message.text.replace('/del', '').strip().split(' ')
    CHAT_IDS = chat_ids
    await message.answer(f"{chat_ids} \n\nHammasini o'chirishni tasdiqlaysizmi?", reply_markup=confirm)


@dp.callback_query_handler(text=['yes', 'no'])
async def my_confirm(call: types.CallbackQuery):
    global CHAT_IDS
    if call.data == 'yes':
        for chat_id in CHAT_IDS:
            users.del_user(chat_id=chat_id)
        await call.message.answer('Operatsiya muvaffaqqiyatli bajarildi!')
    else:
        await call.message.answer('Operatsiya bekor qilindi.')