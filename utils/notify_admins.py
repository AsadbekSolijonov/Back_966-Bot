import logging

from aiogram import Dispatcher

from data.config import ADMINS
from handlers.users.translater import Translater

trr = Translater()


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            datas = trr.get_data_by_language(chat_id=admin)
            await dp.bot.send_message(admin, datas.get('command_start'))

        except Exception as err:
            logging.exception(err)
