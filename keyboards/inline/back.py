from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def custom_back_button(callback_data: str, text: str = '◀ Back') -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=f'{callback_data}')


def custom_back_keyboard(callback_data: str, text: str = '◀ Back') -> InlineKeyboardMarkup:
    button = custom_back_button(callback_data=callback_data, text=text)
    kbd = InlineKeyboardMarkup(row_width=1)
    kbd.add(button)
    return kbd


back_button = custom_back_button(callback_data='back')
back_keyboard = custom_back_keyboard(callback_data='back')
