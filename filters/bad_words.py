from aiogram.filters import BaseFilter
from aiogram import types
from loader import bot
BAD_WORDS = ['iflos','maraz','http','🖕','axmoq']
class CheckMessage(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        admins = await bot.get_chat_administrators(message.chat.id)
        ids = []
        for i in admins:
            ids.append(i.user.id)
        if message.from_user.id in ids:
            pass
        else:
            checks = []
            if message.text:
                text = message.text
                text = text.lower()
                for i in BAD_WORDS:
                    if i in text:
                        checks.append(True)
                    else:
                        checks.append(False)

                if True in checks:
                    return True
                else:
                    return False



