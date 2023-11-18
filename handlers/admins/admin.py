from loader import dp,bot
from  aiogram import types,F
from filters import *
from aiogram.filters import Command
from keyboards.default.buttons import *
from aiogram.fsm.context import FSMContext
from api import get_users,get_groups
@dp.message(Command('admin'),IsChatAdmin(),IsPrivate())
async def start_admin_panel(message:types.Message):
    await message.answer("🔝 Admin panel!",reply_markup=admin_button())
@dp.message(F.text=='🗣 Reklama yuborish',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Kimga xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=group_or_user_button())
@dp.message(F.text=='👤 Foydalanuvchilarga',IsChatAdmin(),IsPrivate())
async def choose_to_whom(message:types.Message,state:FSMContext):
    await state.update_data({
        'send':'user'
    })
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='👥 Guruhlarga',IsChatAdmin(),IsPrivate())
async def choose_to_whom(message:types.Message,state:FSMContext):
    await state.update_data({
        'send':'group'
    })
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
# Back Button
@dp.message(F.text=='⏺ Bekor qilish',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='🆗 Kerakmas',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    await message.answer("Qaysi turdagi xabar yuborasiz!\n"
                         "Tanlang👇",reply_markup=add_type())
@dp.message(F.text=='📊 Obunachilar soni',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    count = len(get_users())
    await message.answer(f"Botda hozir {count} ta faol obunachi bor!")
@dp.message(F.text=='📊 Guruhlar soni',IsChatAdmin(),IsPrivate())
async def get_add_type(message:types.Message):
    count = len(get_groups())
    await message.answer(f"Botda hozir {count} ta faol guruh bor!")



