import asyncio
import logging

from database import Base, get_session
import handlers
from loader import dp, bot
from middlewares import *
from utils import on_startup_notify, set_default_commands


async def on_startup():
    logging.info('DB connecting...')
    db_session = await get_session(db_uri='sqlite+aiosqlite:///db.db')
    logging.info('DB connected!')
    # middlewares
    logging.info('Setting up middlewares...')
    dp.setup_middleware(DBMiddleware(db_session))
    dp.setup_middleware(UserMiddleware())

    logging.info('Everything is ready to launch!')
    # Set default commands (/start and /help)
    await set_default_commands(dp)

    # Notify admin that the bot has started
    await on_startup_notify(dp)
    await dp.skip_updates()
    await dp.start_polling()


async def on_shutdown():
    logging.info('Shutting down...')
    await dp.storage.close()
    await dp.storage.wait_closed()
    bot_session = await bot.get_session()
    await bot_session.close()


async def main():
    try:
        await on_startup()
    finally:
        await on_shutdown()


if __name__ == '__main__':
    # Launch bot
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
