from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons = [
    InlineKeyboardButton(text='📢 Рассылка', callback_data='broadcast'),
    InlineKeyboardButton(text='👤 Пользователи', callback_data='users')
]

admin_keyboard = InlineKeyboardMarkup(row_width=1)
admin_keyboard.add(*buttons)
