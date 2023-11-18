from loader import dp,bot
from  aiogram import types,F
from filters import *
from aiogram.filters import Command
from keyboards.default.buttons import *
from states.mystate import *
from api import get_users
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='⬅️ Orqaga',IsChatAdmin(),IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='◀️ Orqaga',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())