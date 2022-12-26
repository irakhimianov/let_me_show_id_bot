import logging

from aiogram import types, Bot
from aiogram.dispatcher import FSMContext


async def edit_message(
        *,
        bot: Bot,
        text: str,
        call: types.CallbackQuery = None,
        reply_markup: types.InlineKeyboardMarkup = None,
        web_preview: bool = False
):
    try:
        state: FSMContext = bot.get('state')
        if state:
            data = await state.get_data()
            chat_id = data.get('chat_id')
            last_message_id = data.get('last_message_id')
        else:
            chat_id = call.message.chat.id
            last_message_id = call.message.message_id
        await bot.edit_message_text(
            text=text,
            chat_id=chat_id,
            message_id=last_message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=web_preview
        )
    except Exception as e:
        logging.error(f'{__name__} - {e}')
        chat_id = call.message.chat.id
        last_message = await bot.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
        )
        last_message_id = last_message.message_id
    finally:
        return chat_id, last_message_id
