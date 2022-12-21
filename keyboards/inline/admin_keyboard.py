from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons = [
    InlineKeyboardButton(text='📢 Broadcast', callback_data='broadcast'),
    InlineKeyboardButton(text='👤 Users', callback_data='users')
]

admin_keyboard = InlineKeyboardMarkup(row_width=1)
admin_keyboard.add(*buttons)
