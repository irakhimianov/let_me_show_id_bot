from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(), chat_type='private')
async def cmd_start(message: types.Message):
    # Command '/start' handler
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = f'👤 Your <b>User ID</b>: <code>{user_id}</code>\n' \
           f'👉 Current <b>Chat ID</b>: <code>{chat_id}</code>\n\n' \
           f'❓ Want to get another <i>user\'s</i> or <i>chat</i> ID?\n' \
           f'👇 Just forward their message right here'
    await message.answer(text=text)
