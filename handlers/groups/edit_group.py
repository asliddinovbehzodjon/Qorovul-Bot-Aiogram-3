import io
from aiogram import types
from aiogram.filters import Command
from filters import IsGroup
from filters.group_admins import AdminFilter
from loader import dp, bot
@dp.message(IsGroup(), Command("set_photo"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1].file_id
    get_file   = await bot.get_file(file_id=photo)
    file = await bot.download(file=get_file,destination=io.BytesIO())
    input_file = types.input_file.BufferedInputFile(file=file.read(),filename='test.jpg')
    #1-usul
    await message.chat.set_photo(photo=input_file)
    await source_message.delete()
    await message.delete()
@dp.message(IsGroup(), Command("set_title"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    await bot.set_chat_title(chat_id=message.chat.id,title=title)
    await source_message.delete()
    await message.delete()
@dp.message(IsGroup(), Command("set_description"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    await message.chat.set_description(description=description)
    await source_message.delete()
    await message.delete()