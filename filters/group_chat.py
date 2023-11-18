from aiogram.filters import BaseFilter
from aiogram import types
# Chatni guruh ekanligini tekshirish
class IsGroup(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in (
            'group',
            'supergroup'
        )
