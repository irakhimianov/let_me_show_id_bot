from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher.filters.builtin import IsReplyFilter, ForwardedMessageFilter

from loader import dp
from utils import get_content_id


SUPPORTED_TYPES = (
    ContentType.ANIMATION, ContentType.AUDIO, ContentType.PHOTO, ContentType.STICKER,
    ContentType.DOCUMENT, ContentType.VIDEO, ContentType.VOICE, ContentType.POLL, ContentType.LOCATION
)


@dp.message_handler(content_types=SUPPORTED_TYPES)
@dp.message_handler(IsReplyFilter, content_types=SUPPORTED_TYPES)
@dp.message_handler(ForwardedMessageFilter, content_types=SUPPORTED_TYPES)
async def content_message(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    content_id = get_content_id(message=message)
    forwarded_from = ''
    if message.forward_from:
        forwarded_from = message.forward_from.id
        forwarded_from = f'♻ Forwarded from <b>User ID</b>: <code>{forwarded_from}</code>\n'
    elif message.forward_from_chat:
        forwarded_from = message.forward_from_chat.id
        forwarded_from = f'♻ Forwarded from <b>Chat ID</b>: <code>{forwarded_from}</code>\n'

    text = f'👤 Your <b>User ID</b>: <code>{user_id}</code>\n' \
           f'👉 Current <b>Chat ID</b>: <code>{chat_id}</code>\n' \
           f'{forwarded_from}' \
           f'{content_id}'
    await message.answer(text=text)


@dp.message_handler()
@dp.message_handler(IsReplyFilter)
@dp.message_handler(ForwardedMessageFilter)
async def any_message(message: types.Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = f'👤 Your <b>User ID</b>: <code>{user_id}</code>\n' \
           f'👉 Current <b>Chat ID</b>: <code>{chat_id}</code>\n'
    await message.answer(text=text)
