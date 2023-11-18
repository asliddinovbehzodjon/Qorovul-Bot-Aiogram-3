import asyncio
import datetime
from aiogram.filters import CommandStart,Command
from currency import get_currency
from aiogram import types
from loader import dp,bot
from filters import IsPrivate,IsGroup,CheckMessage
from aiogram.filters import ChatMemberUpdatedFilter,IS_NOT_MEMBER,ADMINISTRATOR
from aiogram import html
from api import create_group
text = "Assalomu alaykum!\nGuruppa hamma ishla joyidami?"
@dp.message(CommandStart(),IsGroup())
async def start(message:types.Message):
    await message.answer(text)
@dp.message(Command('kurs'),IsGroup())
async def start(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text=get_currency())
@dp.message(IsGroup(),CheckMessage())
async def punish(message:types.Message):
    text = html.link(value=message.from_user.full_name,link=f"tg://user?id={message.from_user.id}")
    data = await message.reply(f'{text}, yomon so\'z ishlatganiz uchun guruhdan haydaldiz!')
    await asyncio.sleep(3)
    # Ban vaqtini hisoblaymiz (hozirgi vaqt + n minut)
    until_date = datetime.datetime.now() + datetime.timedelta(seconds=5)
    await message.chat.ban(user_id=message.from_user.id,until_date=until_date)

    await message.delete()
    await data.delete()
# Write groups
@dp.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=IS_NOT_MEMBER >> ADMINISTRATOR
    )
)
async def bot_added_as_admin(event: types.ChatMemberUpdated):
    try:
        create_group(name=event.chat.title,telegram_id=event.chat.id)
    except:
        pass
    data = await event.answer(
        text=f"Assalomu alaykum! Meni guruhga qo'shganiz uchun rahmat!\n"
             f"Ishonchizni oqlayman boss!"

    )
    await asyncio.sleep(5)
    await data.delete()
