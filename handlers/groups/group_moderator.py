import asyncio
import datetime
import re
import aiogram
from aiogram import types
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest
from filters import IsGroup, AdminFilter
from loader import dp, bot
# /cheklov yoki !cheklov  komandalari uchun handler
# foydalanuvchini read-only ya'ni faqat o'qish rejimiga o'tkazib qo'yamiz.
@dp.message(IsGroup(), Command("cheklov"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!cheklov|/cheklov) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    # 5-minutga izohsiz cheklash
    # !cheklov 5
    # command='!cheklov' time='5' comment=[]

    # 50 minutga izoh bilan cheklash
    # !cheklov 50 reklama uchun ban
    # command='!cheklov' time='50' comment=['reklama', 'uchun', 'ban']

    time = int(time)
    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    # until_date = datetime.datetime.now() + datetime.timedelta(seconds=time)
    # print(datetime.datetime.now())
    # print(until_date)
    try:
        user_allowed = types.ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_invite_users=False,
            can_change_info=False,
            can_pin_messages=False,
        )
        await message.reply_to_message.delete()
        await message.delete()
        await message.chat.restrict(user_id=member_id,permissions=user_allowed)
        info = await message.answer(
            f"Foydalanuvchi {message.reply_to_message.from_user.full_name} {time} sekund yozish huquqidan mahrum qilindi.\n"
)

        service_message = await message.answer("Xabar 5 sekunddan so'ng o'chib ketadi.")
        await asyncio.sleep(time)
        user_allowed = types.ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=False,
            can_send_polls=False,
            can_send_other_messages=False,
            can_add_web_page_previews=False,
            can_invite_users=False,
            can_change_info=False,
            can_pin_messages=False,
        )
        await service_message.delete()
        await info.delete()
        await message.chat.restrict(user_id=member_id, permissions=user_allowed)

    except TelegramBadRequest as err:
        print(err)
        await message.answer(f"Xatolik! {err.args}")
        return


# read-only holatdan qayta tiklaymiz
@dp.message(IsGroup(), Command("uncheklov"), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    await message.reply_to_message.delete()
    await message.delete()
    service_message = await message.answer("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await message.chat.restrict(user_id=member_id, permissions=user_allowed, until_date=0)
    await message.reply(f"Foydalanuvchi {member.full_name} tiklandi")

    # xabarlarni o'chiramiz
    await message.delete()
    await service_message.delete()

# Foydalanuvchini banga yuborish (guruhdan haydash)
@dp.message(IsGroup(), Command("ban"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.kick(user_id=member_id)

    await message.answer(f"Foydalanuvchi {message.reply_to_message.from_user.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")

    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()

