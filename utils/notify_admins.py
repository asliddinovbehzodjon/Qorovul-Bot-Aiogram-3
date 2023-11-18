from data.config import ADMINS,BOT
from aiogram import Dispatcher
from loader import bot
import logging

async def on_startup_notify():
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text="Bot ishga tushdi!")
        except Exception as Err:
            logging.exception(Err)
async def on_shutdown_notify():
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text="Bot to'xtadi!")
        except Exception as Err:
            logging.exception(Err)
