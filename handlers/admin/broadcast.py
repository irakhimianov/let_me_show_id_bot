import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from database import User, requests
from filters import IsAdmin
from keyboards.inline import cancel_keyboard, admin_keyboard
from loader import dp, bot
from states import BroadcastState
from utils import edit_message


@dp.callback_query_handler(IsAdmin(), text='broadcast')
async def broadcast(call: types.CallbackQuery, state: FSMContext):
    """
    Broadcast callback handler
    :param call:
    :return:
    """
    text = '💥 Send your text for broadcast:'
    chat_id, last_message_id = await edit_message(
        bot=bot,
        text=text,
        call=call,
        reply_markup=cancel_keyboard
    )
    bot['state'] = state
    async with state.proxy() as data:
        data['chat_id'] = chat_id
        data['last_message_id'] = last_message_id
    await BroadcastState.text.set()
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.message_handler(IsAdmin(), state=BroadcastState.text)
async def broadcast_text(message: types.Message, session: AsyncSession, state: FSMContext):
    """
    Handler to get the broadcast text
    :param message:
    :param state:
    :param session:
    :return:
    """
    logging.info(f'Broadcast by {message.from_user.id}')
    users = await requests.get_users(session=session)
    users = [user for user in users]

    for user in users:
        user: User
        try:
            await bot.send_message(chat_id=user.user_id, text=message.text)
            if not user.is_active:
                await requests.update_user(user_id=user.user_id, is_active=False, session=session)
        except Exception as e:
            await requests.update_user(user_id=user.user_id, is_active=True, session=session)
            logging.error(f'{user.user_id} - {e}')
    await state.finish()
    await message.answer(text='✅ Broadcast completed', reply_markup=admin_keyboard)
