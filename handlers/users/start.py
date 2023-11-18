from aiogram.filters import CommandStart,Command
from aiogram import types
from loader import dp,bot
from filters import IsPrivate
from data.config import BOT
from api import create_user
@dp.message(CommandStart(),IsPrivate())
async def start(message:types.Message):
    try:
        create_user(name=message.from_user.full_name,telegram_id=message.from_user.id)
    except:
        pass
    text = (f"Assalomu alaykum!\n"
            f"Boss,Men Oliy Ma'lumotli Qorovul botman!\n"
            f"Meni guruhizga qo'shing va oyogizni cho'zib dam oling!Qolgani meni zimmamda!\n")
    from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton
    button = InlineKeyboardBuilder()
    button.button(text="Guruhga qo'shish",url=f'https://t.me/{BOT}?startgroup=true')

    await message.answer(text=text,reply_markup=button.as_markup())
