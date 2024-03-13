from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(message: types.Message):
    await message.answer('Siz document yubordingiz!')
    await message.answer(f"{message}")
    # 1-usul send file
    # await message.bot.send_document(chat_id=message.chat.id,
    #                                 document=f"{message.document.file_id}",
    #                                 caption=f"{message.document.file_name}")
    # 2-usul send file
    # await message.answer_document(document=f"{message.document.file_id}", caption=f"{message.document.file_name}!")
    # download
    file_id = message.document.file_id
    download = await message.bot.get_file(file_id)
    await download.download()


@dp.message_handler(commands=['send_to_all_students'])
async def send_book(message: types.Message):
    # 3-usul send file
    for chat_id in [6739253356, 2044476906, 5988874328, 1718706422, 6771458437, 381748791]:
        try:
            await message.bot.send_document(chat_id=chat_id, document=open('documents/file_2.pdf', 'rb'),
                                            caption='Talabalar shu shartnomani toldirib beringlar')
        except Exception as e:
            await message.answer(f"{chat_id} topilmadi!")
    await message.answer('Xabarlar barcha studentlar uchun yuborildi!')

