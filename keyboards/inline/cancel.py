from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def custom_cancel_button(callback_data: str, text: str = '❌ Cancel') -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, callback_data=f'{callback_data}')


def custom_cancel_keyboard(callback_data: str, text: str = '❌ Cancel') -> InlineKeyboardMarkup:
    button = custom_cancel_button(callback_data=callback_data, text=text)
    kbd = InlineKeyboardMarkup(row_width=1)
    kbd.add(button)
    return kbd


cancel_button = custom_cancel_button(callback_data='cancel')
cancel_keyboard = custom_cancel_keyboard(callback_data='cancel')
