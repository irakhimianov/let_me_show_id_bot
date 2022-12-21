from aiogram import types
from aiogram.types import BotCommandScopeChat, BotCommandScopeDefault
from aiogram import Dispatcher

from data.config import ADMIN


async def set_default_commands(dp: Dispatcher) -> None:
    # Pop-up tips when '/' is typed in chat-window with bot
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Start bot'),
            types.BotCommand('help', 'Help'),
            types.BotCommand('admin', 'Admin menu')
        ],
        scope=BotCommandScopeChat(chat_id=ADMIN)
    )

    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Start bot'),
            types.BotCommand('help', 'Help'),
        ],
        scope=BotCommandScopeDefault()
    )
