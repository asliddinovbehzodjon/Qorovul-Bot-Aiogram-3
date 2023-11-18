from aiogram import types
from aiogram.filters import BaseFilter
from loader import bot

class ChatJoined(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message.new_chat_members:
            return True
        else:
            return False
class ChatLeft(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        if message.left_chat_member:
            return True
        else:
            return False