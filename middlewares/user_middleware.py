from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from database import requests


class UserMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        await self.process_user(message.from_user, data)

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        await self.process_user(call.from_user, data)

    async def process_user(self, user: types.User, data: dict):
        username = user.username if user.username else f'Пользователь id {user.id}'
        await requests.add_user(user_id=user.id, session=data['session'])
