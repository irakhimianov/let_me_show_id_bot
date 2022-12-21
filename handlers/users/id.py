from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from loader import dp


@dp.message_handler(chat_type='private', commands=['id'])
@dp.message_handler(IsGroup(), commands=['id'])
@dp.channel_post_handler(IsGroup(), Command(['id']))
async def get_id(message: types.Message):
    user_id = ''
    if message.sender_chat is None:
        user_id = f'👤 Your <b>User ID</b>: <code>{message.from_user.id}</code>\n'
    text = f'{user_id}' \
           f'👉 Current <b>{message.chat.type.capitalize()} Chat ID</b>: <code>{message.chat.id}</code>'
    await message.answer(text=text)
