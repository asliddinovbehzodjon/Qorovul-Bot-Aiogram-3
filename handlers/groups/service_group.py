import asyncio
from filters import IsGroup,ChatJoined,ChatLeft
from loader import dp, bot
from aiogram import types,F,html
from  aiogram import html
from aiogram.filters import IS_MEMBER,IS_NOT_MEMBER,ChatMemberUpdatedFilter,MEMBER
rules = ("Iltimos guruhda ushbu qoidalarga amal qiling:\n"
         "1️⃣.Bir biringizga hurmat bo'ling!\n"
         "2️⃣.Yomon so'zlarni ishlatmang.Masalan: axmoq.Aks holda🚀.\n"
         "3️⃣.Yuqoridagi 2 ta qoidaga amal qiling.")
@dp.message(F.new_chat_members)
async def new(message:types.Message):
      members = ", ".join([html.link(value=m.first_name,link=f'tg://user?id={m.id}') for m in message.new_chat_members])
      await message.delete()
      data = await message.answer(f"Xush kelibsiz, {members}.")
      await asyncio.sleep(3)
      await data.delete()
@dp.message(F.left_chat_member)
async def new(message:types.Message):
    await message.delete()
    if message.left_chat_member.id == message.from_user.id:
        data = await message.answer(f"{html.link(value=message.left_chat_member.first_name,link=f'tg://user?id={message.left_chat_member.id}')} guruhni tark etdi")
    else:
        data = await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi ")
    await asyncio.sleep(3)
    await data.delete()

