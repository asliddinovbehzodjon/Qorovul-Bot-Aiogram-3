from aiogram import types
from aiogram.filters import BaseFilter
from loader import bot

# Request(So'rov yuborgan shaxs guruhda admin yoki admin masligini tekshirish)
class AdminFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        member = await message.chat.get_member(message.from_user.id)
        return member.status.ADMINISTRATOR and member.status.CREATOR