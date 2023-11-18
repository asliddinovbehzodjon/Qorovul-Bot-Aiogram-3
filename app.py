import middlewares, filters, handlers
import asyncio
import logging
import sys
from utils.notify_admins import on_startup_notify,on_shutdown_notify
from utils.set_bot_commands import *
from loader import dp, bot
from middlewares.throttling import ThrottlingMiddleware
async def main():
    await set_group_commands()
    await set_private_commands()
    # dp.update.middleware.register(ThrottlingMiddleware())
    try:
        dp.startup.register(on_startup_notify)
        dp.shutdown.register(on_shutdown_notify)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())