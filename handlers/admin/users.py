from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from database import requests
from filters import IsAdmin
from keyboards.inline import users_keyboard, custom_back_keyboard
from loader import bot, dp
from utils import edit_message


@dp.callback_query_handler(IsAdmin(), text='users', state='*')
async def get_users_list(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    users = await requests.get_users(session=session)
    paginator = users_keyboard(users=users)
    args, kwargs = paginator.paginator_handler()
    dp.register_callback_query_handler(*args, **kwargs)
    text = '👤 Users list'
    await edit_message(
        bot=bot,
        text=text,
        state=state,
        reply_markup=paginator()
    )
    await bot.answer_callback_query(callback_query_id=call.id)


@dp.callback_query_handler(IsAdmin(), text_contains='get_user_by_id_', state='*')
async def get_user(call: types.CallbackQuery, session: AsyncSession, state: FSMContext):
    user_id = int(call.data.split('_')[-1])
    user = await requests.get_user(user_id=user_id, session=session)
    text = f'<u><b>User:</b></u> <a href="tg://user?id={user.user_id}">{user.user_id}</a>\n'
    await edit_message(
        bot=bot,
        text=text,
        state=state,
        reply_markup=custom_back_keyboard(callback_data='users')
    )
    await bot.answer_callback_query(callback_query_id=call.id)
