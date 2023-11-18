from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from data import config

bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML)
stroge = MemoryStorage()
dp = Dispatcher(storage=stroge)