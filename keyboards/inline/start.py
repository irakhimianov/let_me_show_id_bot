from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def custom_inline_button(text: str = '👉 TRY INLINE MODE 👈') -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, switch_inline_query_current_chat='')


def custom_inline_keyboard(text: str = '👉 TRY INLINE MODE 👈') -> InlineKeyboardMarkup:
    button = custom_inline_button(text=text)
    kbd = InlineKeyboardMarkup(row_width=1)
    kbd.add(button)
    return kbd


start_button = custom_inline_button()
start_keyboard = custom_inline_keyboard()
