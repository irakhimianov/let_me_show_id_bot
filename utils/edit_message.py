import logging

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import (MessageNotModified, MessageToEditNotFound, ChatNotFound,
                                      MessageIdentifierNotSpecified, ChatIdIsEmpty)


async def edit_message(
        *,
        bot: Bot,
        text: str,
        state: FSMContext = None,
        chat_id: int = None,
        last_message_id: int = None,
        reply_markup: types.InlineKeyboardMarkup = None,
        web_preview: bool = False
):
    if state and (chat_id is last_message_id is None):
        data = await state.get_data()
        chat_id = data.get('chat_id')
        last_message_id = data.get('last_message_id')
    try:
        await bot.edit_message_text(
            text=text,
            chat_id=chat_id,
            message_id=last_message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=web_preview
        )
    except MessageNotModified as e:
        logging.error(f'{__name__} - {e}')
    except (MessageIdentifierNotSpecified, MessageToEditNotFound, ChatNotFound, ChatIdIsEmpty) as e:
        logging.error(f'{__name__} - {e}')
        last_message = await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup
        )
        if state:
            async with state.proxy() as data:
                data['chat_id'] = chat_id
                data['last_message_id'] = last_message.message_id
