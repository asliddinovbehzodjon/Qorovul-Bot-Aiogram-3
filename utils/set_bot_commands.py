from aiogram import types
from loader import bot
from aiogram.types.bot_command_scope_all_group_chats import BotCommandScopeAllGroupChats
from aiogram.types.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
async def set_group_commands():
    await bot.set_my_commands(
        [

            types.BotCommand(command='kurs', description='Pul kursi'),

        ],
        scope=BotCommandScopeAllGroupChats(type='all_group_chats')
    )
async def set_private_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='Restart the bot'),

        ],
        scope=BotCommandScopeAllPrivateChats(type='all_private_chats')
    )