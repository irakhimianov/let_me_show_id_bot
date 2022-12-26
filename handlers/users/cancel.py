from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from loader import dp, bot


@dp.callback_query_handler(chat_type='private', text_contains='cancel', state='*')
async def call_cancel(call: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )
    text = '❌ <b>Last operation canceled</b>'
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=text,
    )
    await state.finish()
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.message_handler(chat_type='private', commands='cancel', state='*')
@dp.message_handler(chat_type='private', text='❌ Cancel', state='*')
@dp.message_handler(IsAdmin(), chat_type='private', commands='cancel', state='*')
@dp.message_handler(IsAdmin(), chat_type='private', text='❌ Cancel', state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    if await state.get_state():
        data = await state.get_data()
        if data.get('chat_id') and data.get('last_message_id'):
            await bot.delete_message(
                chat_id=data['chat_id'],
                message_id=data['last_message_id']
            )
        await state.finish()
    text = '❌ <b>Last operation canceled</b>'
    await bot.send_message(chat_id=message.chat.id, text=text)
