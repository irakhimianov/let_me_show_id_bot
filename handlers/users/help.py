from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    # Command '/help' handler
    text = f'I will show you your <b>telegram user ID</b>, <b>current chat ID</b> and <b>ID</b> of forwarded message.'\
           f'\n<i>User telegram ID</i>, <i>Chat ID</i> - unique identifier of telegram objects such as ' \
           f'User, Bot, Chat etc.\n Read more: https://core.telegram.org/bots/api#user\n' \
           f'Supported message\'s content: <i>animtaion, audio, document, location, photo, poll, ' \
           f'sticker, video, voice</i>'
    await message.answer(text=text)
