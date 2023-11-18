from aiogram.filters import BaseFilter
from aiogram import types
class IsPrivate(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:

        return message.chat.type in (
            'private'
        )
