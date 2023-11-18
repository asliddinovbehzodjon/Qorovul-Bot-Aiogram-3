from aiogram.filters import BaseFilter
from aiogram import types
from data.config import ADMINS
class IsChatAdmin(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if str(message.from_user.id) in ADMINS:
            return True
        else:
            return False