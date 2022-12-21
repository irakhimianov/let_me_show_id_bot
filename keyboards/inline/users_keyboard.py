from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .back import custom_back_button
from database import User
from utils import Paginator


def users_keyboard(users: list[User]) -> Paginator:
    kb = InlineKeyboardMarkup(row_width=1)
    buttons = []
    for user in users:
        user: User
        buttons.append(
            InlineKeyboardButton(
                text=f'{user.user_id}',
                callback_data=f'get_user_by_id_{user.user_id}')
        )
    kb.add(*buttons)
    paginator = Paginator(data=kb, size=5, back_button=custom_back_button(callback_data='admin'))
    return paginator
