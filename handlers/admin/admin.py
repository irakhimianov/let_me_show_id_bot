from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from loader import dp, bot
from keyboards.inline import admin_keyboard
from utils import edit_message


@dp.message_handler(IsAdmin(), commands='admin')
async def admin(message: types.Message, state: FSMContext):
    last_message = await message.answer(
        text='Админ-меню',
        reply_markup=admin_keyboard
    )
    async with state.proxy() as data:
        data['chat_id'] = message.chat.id
        data['last_message_id'] = last_message.message_id


@dp.callback_query_handler(IsAdmin(), text='admin')
async def call_admin(call: types.CallbackQuery, state: FSMContext):
    text = 'Админ-меню'
    await edit_message(
        bot=bot,
        text=text,
        reply_markup=admin_keyboard,
        state=state
    )
    await bot.answer_callback_query(callback_query_id=call.id)